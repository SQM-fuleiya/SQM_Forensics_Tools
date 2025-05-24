import frida, sys

jscode = """
Java.perform(function () {
    var Myclass= Java.use('这里填写要Hook的类名');          //这里写要Hook的软件的类名，建议配合jadx和JEB使用
    Myclass.Mymethod.implementation = function (str) {    //这里写要Hook的类下的方法名Mymethod
        send('Hook success');                             //这里是输出打印相关的提示语结果
        console.log('string is: ' + str));
    };
});
"""

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

process = frida.get_remote_device().attach('这里写软件的包名')  # 这里写要Hook的软件的包名
# pid = device.spawn(["com.android.chrome"])
# session = device.attach(pid)
# device.resume(pid)
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Hook Start Running')
script.load()
sys.stdin.read()
