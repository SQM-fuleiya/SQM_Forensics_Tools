Java.perform(function () {
    // Hook java.lang.String 构造方法
    var StringClass = Java.use('java.lang.String');

    // Hook 字节数组构造方法
    StringClass.$init.overload('[B').implementation = function (bytes) {
        var result = this.$init(bytes);
        console.log("[String from byte array] " + this.toString());
        return result;
    };

    // Hook 字符数组构造方法
    StringClass.$init.overload('[C').implementation = function (chars) {
        var result = this.$init(chars);
        console.log("[String from char array] " + this.toString());
        return result;
    };

    // Hook 普通字符串构造方法
    StringClass.$init.overload('java.lang.String').implementation = function (str) {
        var result = this.$init(str);
        console.log("[String from another String] " + this.toString());
        return result;
    };

    // Hook Resources 类获取字符串的方法
    var ResourcesClass = Java.use('android.content.res.Resources');

    // Hook getString(int resId) 方法
    ResourcesClass.getString.overload('int').implementation = function (resId) {
        var result = this.getString(resId);
        console.log("[Resource String] ID: " + resId + ", Value: " + result);
        return result;
    };

    // Hook getString(int resId, Object... formatArgs) 方法
    ResourcesClass.getString.overload('int', '[Ljava.lang.Object;').implementation = function (resId, formatArgs) {
        var result = this.getString(resId, formatArgs);
        console.log("[Resource String with format] ID: " + resId + ", Value: " + result);
        return result;
    };
});
