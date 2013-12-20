function Class() {};
Class.prototype.extend = function(props) {
	var SubClass = function() {};
	SubClass.prototype = Object.create(this.prototype);
	SubClass.prototype.constructor = SubClass;
	SubClass.extend = SubClass.prototype.exted;
	SubClass.create = SubClass.prototype.create;
	return SubClass;
};
Class.prototype.create = function(props) {
	var instance = new this();
	for (var i in props) {
		instance[i] = props[i];
	}
	return instance;
};
Class.extend = function(props) {
	return this.prototype.extend.call(this, props);
};
var Human = Class.extend({
	say: function() {}
});
var c = Human.create({
	test: function() {

	}
});
console.dir(c);


function Test(props) {
	var instance = function() {};
	for (var i in props) {
		instance[i] = props[i];
	}
	instance.prototype.init = function() {};
	return instance;
};
Test.prototype.init = function() {};
Test.create = function() {
	return new this();
};

var t = Test.create();
console.dir(t);