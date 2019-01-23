var yaml = require('js-yaml');
var writeyaml = require('write-yaml');
var fs = require('fs');

try{
	var doc = yaml.safeLoad(fs.readFileSync('variables.yml'));
	console.log(doc);
	}
catch (e) {
	console.log(e);
}
newdata = {'hey': 01,
		'david' : 02,
		'whatup': 03}


try{
	writeyaml.sync('variables.yml', newdata);	

}
catch (e) {
	console.log(e);
}
