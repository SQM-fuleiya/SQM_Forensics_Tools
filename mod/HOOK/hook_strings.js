// 读取全部字符串并打印

Java.perform(function () {
    // Hook java.lang.String 类的构造函数
    Java.choose("java.lang.String", {
        // 当找到匹配的对象时执行
        onMatch: function (instance) {
            try {
                // 获取字符串的值
                var strValue = instance.toString();
                // 打印字符串
                console.log("Hooked String: " + strValue);
            } catch (e) {
                console.error("获取字符串值时出错: " + e);
            }
        },
        // 所有匹配完成后执行
        onComplete: function () {
            console.log("字符串 HOOK 已完成");
        }
    });

    // Hook 常用的字符串创建方法
    var StringClass = Java.use('java.lang.String');

    // Hook 构造函数
    StringClass.$init.overload('[B').implementation = function (bytes) {
        var result = this.$init(bytes);
        var str = this.toString();
        console.log("HOOK 字符串函数 (byte[]): " + str);
        return result;
    };

    StringClass.$init.overload('[B', 'int', 'int').implementation = function (bytes, offset, length) {
        var result = this.$init(bytes, offset, length);
        var str = this.toString();
        console.log("HOOK 字符串函数 (byte[], int, int): " + str);
        return result;
    };

    StringClass.$init.overload('[C').implementation = function (chars) {
        var result = this.$init(chars);
        var str = this.toString();
        console.log("HOOK 字符串函数 (char[]): " + str);
        return result;
    };

    StringClass.$init.overload('[C', 'int', 'int').implementation = function (chars, offset, count) {
        var result = this.$init(chars, offset, count);
        var str = this.toString();
        console.log("HOOK 字符串函数 (char[], int, int): " + str);
        return result;
    };

    // Hook String.valueOf 方法
    StringClass.valueOf.overload('char').implementation = function (c) {
        var result = this.valueOf(c);
        console.log("Hooked String.valueOf(char): " + result);
        return result;
    };

    StringClass.valueOf.overload('boolean').implementation = function (b) {
        var result = this.valueOf(b);
        console.log("Hooked String.valueOf(boolean): " + result);
        return result;
    };

    StringClass.valueOf.overload('int').implementation = function (i) {
        var result = this.valueOf(i);
        console.log("Hooked String.valueOf(int): " + result);
        return result;
    };

    StringClass.valueOf.overload('long').implementation = function (l) {
        var result = this.valueOf(l);
        console.log("Hooked String.valueOf(long): " + result);
        return result;
    };

    StringClass.valueOf.overload('float').implementation = function (f) {
        var result = this.valueOf(f);
        console.log("Hooked String.valueOf(float): " + result);
        return result;
    };

    StringClass.valueOf.overload('double').implementation = function (d) {
        var result = this.valueOf(d);
        console.log("Hooked String.valueOf(double): " + result);
        return result;
    };

    StringClass.valueOf.overload('java.lang.Object').implementation = function (obj) {
        var result = this.valueOf(obj);
        console.log("Hooked String.valueOf(Object): " + result);
        return result;
    };
});
