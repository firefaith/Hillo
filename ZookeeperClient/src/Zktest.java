import java.io.IOException;

import org.apache.zookeeper.CreateMode;
import org.apache.zookeeper.ZooDefs.Ids;
import org.apache.zookeeper.ZooKeeper;


public class Zktest {

	public static void main(String[] args) {
		String usage="1- connect,e.g. host:port \n2- session,e.g. 10000,\n3- zkpath,e.g. /nileader";
		if(args.length!=3){System.out.println(usage);return;}
		else{
			String con=args[0];
	    	int session=Integer.parseInt(args[1]);
	    	String zkpath=args[2];
	    			
	    	System.out.println(con+","+session);
	    	
	    	try {
				ZooKeeper zk = new ZooKeeper(con, session, null);
			
				
				while(!zk.getState().isConnected()){}
				
					String apath=zk.create(zkpath, "mydata".getBytes(), Ids.OPEN_ACL_UNSAFE, CreateMode.PERSISTENT);
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

	}

}
