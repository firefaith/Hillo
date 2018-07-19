import ConfigParser, os

config = ConfigParser.SafeConfigParser({'h1':{"a2":3}})
config.readfp(open('defaults.conf'))
print config.get("h1","a1")
print config.get("h1","a2")
