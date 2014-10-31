package com.ucloud.zkcli;

import java.io.IOException;
import java.util.concurrent.CountDownLatch;

import org.apache.zookeeper.CreateMode;
import org.apache.zookeeper.KeeperException;
import org.apache.zookeeper.WatchedEvent;
import org.apache.zookeeper.Watcher;
import org.apache.zookeeper.Watcher.Event.KeeperState;
import org.apache.zookeeper.ZooDefs.Ids;
import org.apache.zookeeper.ZooKeeper;
import org.apache.zookeeper.ZooKeeperMain;
	
public class WatchExample implements Watcher{

	    private static final int SESSION_TIMEOUT = 10000; 
	    private static final String CONNECTION_STRING = "61.153.100.95:2181"; 
	    private static final String ZK_PATH = "/nileader"; 
	    private ZooKeeper zk = null;      
	    private CountDownLatch connectedSemaphore = new CountDownLatch( 1 ); 
	 
	    /** 
	     * ����ZK���� 
	     * @param connectString  ZK��������ַ�б� 
	     * @param sessionTimeout   Session��ʱʱ�� 
	     */ 
	    public void createConnection( String connectString, int sessionTimeout ) { 
	        this.releaseConnection(); 
	        try { 
	            zk = new ZooKeeper( connectString, sessionTimeout, this ); 
	           // connectedSemaphore.await(); 
	        } /*catch ( InterruptedException e ) { 
	            System.out.println( "���Ӵ���ʧ�ܣ����� InterruptedException" ); 
	            e.printStackTrace(); 
	        }*/ catch ( Exception e ) { 
	            System.out.println( "���Ӵ���ʧ�ܣ����� IOException" ); 
	            e.printStackTrace(); 
	        } 
	    } 
	 
	    /** 
	     * �ر�ZK���� 
	     */ 
	    public void releaseConnection() { 
	        if ( null != (this.zk)  ) { 
	            try { 
	                this.zk.close(); 
	            } catch ( InterruptedException e ) { 
	                // ignore 
	                e.printStackTrace(); 
	            } 
	        } 
	    } 
	 
	    /** 
	     *  �����ڵ� 
	     * @param path �ڵ�path 
	     * @param data ��ʼ�������� 
	     * @return 
	     */ 
	    public boolean createPath( String path, String data ) { 
	        try { 
	            System.out.println( "�ڵ㴴���ɹ�, Path: " 
	                    + this.zk.create( path, // 
	                                              data.getBytes(), // 
	                                              Ids.OPEN_ACL_UNSAFE, // 
	                                              CreateMode.EPHEMERAL ) 
	                    + ", content: " + data ); 
	        } catch ( KeeperException e ) { 
	            System.out.println( "�ڵ㴴��ʧ�ܣ�����KeeperException" ); 
	            e.printStackTrace(); 
	        } catch ( InterruptedException e ) { 
	            System.out.println( "�ڵ㴴��ʧ�ܣ����� InterruptedException" ); 
	            e.printStackTrace(); 
	        } 
	        return true; 
	    } 
	 
	    /** 
	     * ��ȡָ���ڵ��������� 
	     * @param path �ڵ�path 
	     * @return 
	     */ 
	    public String readData( String path ) { 
	        try { 
	            System.out.println( "��ȡ���ݳɹ���path��" + path ); 
	            return new String( this.zk.getData( path, false, null ) ); 
	        } catch ( KeeperException e ) { 
	            System.out.println( "��ȡ����ʧ�ܣ�����KeeperException��path: " + path  ); 
	            e.printStackTrace(); 
	            return ""; 
	        } catch ( InterruptedException e ) { 
	            System.out.println( "��ȡ����ʧ�ܣ����� InterruptedException��path: " + path  ); 
	            e.printStackTrace(); 
	            return ""; 
	        } 
	    } 
	 
	    /** 
	     * ����ָ���ڵ��������� 
	     * @param path �ڵ�path 
	     * @param data  �������� 
	     * @return 
	     */ 
	    public boolean writeData( String path, String data ) { 
	        try { 
	            System.out.println( "�������ݳɹ���path��" + path + ", stat: " + 
	                                                        this.zk.setData( path, data.getBytes(), -1 ) ); 
	        } catch ( KeeperException e ) { 
	            System.out.println( "��������ʧ�ܣ�����KeeperException��path: " + path  ); 
	            e.printStackTrace(); 
	        } catch ( InterruptedException e ) { 
	            System.out.println( "��������ʧ�ܣ����� InterruptedException��path: " + path  ); 
	            e.printStackTrace(); 
	        } 
	        return false; 
	    } 
	 
	    /** 
	     * ɾ��ָ���ڵ� 
	     * @param path �ڵ�path 
	     */ 
	    public void deleteNode( String path ) { 
	        try { 
	            this.zk.delete( path, -1 ); 
	            System.out.println( "ɾ���ڵ�ɹ���path��" + path ); 
	        } catch ( KeeperException e ) { 
	            System.out.println( "ɾ���ڵ�ʧ�ܣ�����KeeperException��path: " + path  ); 
	            e.printStackTrace(); 
	        } catch ( InterruptedException e ) { 
	            System.out.println( "ɾ���ڵ�ʧ�ܣ����� InterruptedException��path: " + path  ); 
	            e.printStackTrace(); 
	        } 
	    } 
	 
	    public static void main( String[] args ) { 
	 
	    	/*WatchExample sample = new WatchExample(); 
	        
	    	sample.createConnection( CONNECTION_STRING, SESSION_TIMEOUT ); 
	        
	        if ( sample.createPath( ZK_PATH, "���ǽڵ��ʼ����" ) ) { 
	            System.out.println(); 
	            System.out.println( "��������: " + sample.readData( ZK_PATH ) + "\n" ); 
	            sample.writeData( ZK_PATH, "���º������" ); 
	            System.out.println( "��������: " + sample.readData( ZK_PATH ) + "\n" ); 
	            sample.deleteNode( ZK_PATH ); 
	        } 
	 
	        sample.releaseConnection(); */
	    	//WatchExample we = new WatchExample();
	    	
	    	String con=args[0];
	    	int session=Integer.parseInt(args[1]);
	    	System.out.println(con+","+session);
	    	
	    	try {
				ZooKeeper zk = new ZooKeeper(con, session, null);
				
				while(!zk.getState().isConnected()){}
				
					String apath=zk.create(ZK_PATH, "mydata".getBytes(), Ids.OPEN_ACL_UNSAFE, CreateMode.PERSISTENT);
					if(apath.length()!=0) System.out.println("create ok,path="+apath);
					else System.out.println("create path failed.");	
				
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	    	
	    	
	    } 
	 
	    /** 
	     * �յ�����Server��Watcher֪ͨ��Ĵ��� 
	     */ 
	    @Override 
	    public void process( WatchedEvent event ) { 
	        System.out.println( "�յ��¼�֪ͨ��" + event.getState() +"\n"  ); 
	        if ( KeeperState.SyncConnected == event.getState() ) { 
	            connectedSemaphore.countDown(); 
	        } 
	 
	    } 

}
	