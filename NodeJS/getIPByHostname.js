var dns = require('dns');

function hostnameLookup(hostname) {
dns.lookup(hostname, function(err, addresses, family){
console.log(addresses);
});
}

if(process.argy.length <=2){
	console.log("USAGE:"+ __filename + "IPADDR")
	process.exit(-1)
}

var hostname = process.argy[2]
console.log('Checking IP of:${hostname}')
hostnameLookup(hostname);
