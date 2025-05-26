
const CryptoJS = require('crypto-js');

function decrypt(I1li1iIi, I1iiIIlI, iliIlI1){
    let lIlIlIl1 = CryptoJS['AES']['decrypt'](I1li1iIi,CryptoJS['enc']['Utf8']['parse'](I1iiIIlI), {
        'iv': CryptoJS['enc']['Utf8']['parse'](iliIlI1),
        'mode': CryptoJS['mode']['CBC'],
        'padding': CryptoJS['pad']['Pkcs7']
    })
    return lIlIlIl1['toString'](CryptoJS['enc']['Utf8']);
}

var sign = function(NowTime , url) {
    string = NowTime + url
    a = CryptoJS.MD5(string).toString();
    var b = CryptoJS.MD5(a);
    var c = CryptoJS.enc.Utf8.parse(b);
    var d = CryptoJS.enc.Utf8.parse('https://t.me/xmflv666');
    var e = CryptoJS.AES.encrypt(a, c, {
        iv: d,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    });
    return e.toString()
}

console.log(sign('1748241435','https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2F324olz7ilvo2j5f%2Ft0035aw2v35.html'))

// Mw = 'UrmxokRjVcKAydXqzvCyL7GvMo1e6ck56/27smieb+yL8gbVbCvjpFSf7mdHdEyEz6O8EliOQKxUSLhV9C0gxk6pY3q7DgQdAWwvuyRCKOwXt/8K4bYHy6S8xIydQHMEcdZRTM6mOKy70O4oQDUytfyS07joloAEadT/q2MKUH4DsXzBVSHLwoKPT8ByCge3ARPRb/+noBnWes04sEjrifxBZIH8rCIKRrJW3zk6n+1eRLekpYYiSYUER6MDdjHeFlwymXrXqCJ83KsvzkxE+OqXd+MA9Zji1FUHn+TLTFGU1nuL3ZoP7vbA7YsrhdyDX5YbZRBIlDTKHL30pc3YWBDVybfkoW+1nsRatFKXGqha3wrVHLyh5GKXIqRXa5kFE7o2dHwkPv/0dtzdphV6neHDlkPIRULwtWv+DBTddmk='
// key = 'zouV0wTKChH8Tjyg'
// IV = 'iY6qQHHbqpOL3MRH'

// console.log(decrypt(Mw,key,IV))