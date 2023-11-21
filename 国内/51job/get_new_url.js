let filter_ls = [], con_count = {};

function hook(o) {
    function hook_apply(obj) {
        obj = new Proxy(obj, {
            get: function (target, p, receiver) { //针对对象
                if (String(p).search(/\d+$/) === -1 && String(p).search(/Symbol/) === -1) {
                    if (!filter_ls.includes(p)) {
                        //   console.log('hook: ', target.toString(), '获取', p, '-->', String(target[p]).replace(/\s/g, '').substring(0, 50));
                        filter_ls.push(p);
                        con_count[p] = 1
                    } else {
                        con_count[p] += 1
                    }
                }
                return target[p];
            },
            set: function (target, p, val) {//针对对象
// console.log('hook: ', target.toString(), '设置：', p, '-->', String(val).replace(/\s/g, '').substring(0, 50));
                //  console.log('hook: ', target.toString(), '设置：', p, '-->', String(val).replace(/\s/g, ''));
                target[p] = val;
            },
            has: function (target, p) { //针对对象
                // console.log('hook: ', target.toString(), '是否包含：', p, '-->', p in target);
                return p in target
            },
            apply: function () { // 针对方法
                if (arguments[1]) {
                    if (typeof arguments[1] == 'string') {
                        res_mapping[arguments[1].substring(0, 30)] = res_mapping[arguments[1].substring(0, 30)] || {
                            vals: [],
                            count: 0
                        }
                        if (res_mapping[arguments[1].substring(0, 30)].count < 4) {
                            //   console.log('hook: ', '函数：', arguments[0].name, '对象：', arguments[1].substring(0, 30), '执行内容：', arguments[2], '结果：', arguments[0].apply(arguments[1], arguments[2]));
                        }
                        res_mapping[arguments[1].substring(0, 30)]['vals'].push(arguments[2])
                        res_mapping[arguments[1].substring(0, 30)]['count']++;
                        // console.log('hook: ', '函数：', arguments[0].name, '对象：', String(arguments[1]).substring(0, 30), '执行内容：', arguments[2], '结果：', arguments[0].apply(arguments[1], arguments[2]));
                    } else {
                        // console.log('hook: ', '函数：', arguments[0].name, '对象：', String(arguments[1]).substring(0, 30), '执行内容：', arguments[2], '结果：', arguments[0].apply(arguments[1], arguments[2]));
                    }
                } else {
                    // console.log('hook: ', '函数：', arguments[0].name, '对象：', arguments[1].substring(0, 30), '执行内容：', arguments[2], '结果：', arguments[0].apply(arguments[1], arguments[2]));
                }
                if (arguments[2][0] == 'body') {
                    return false
                } else {
                    return arguments[0].apply(arguments[1], arguments[2])
                }
            },
            ownKeys: function (_o) {
                //  console.log('循环遍历：', Object.keys(_o).slice(0, 10));
                return Object.keys(_o);
            }
        })
        return obj;
    }

    if (typeof o.hasOwnProperty != 'undefined') {
        o.hasOwnProperty = hook_apply(o.hasOwnProperty)
    }
    o = hook_apply(o);
    return o;
}

canvas = {
    getContext: function (content) {
        if (content.indexOf('webgl') !== -1) {
            return false
        } else {
            return CanvasRenderingContext2D
        }
    },
    toDataURL: function () {
// 实际为canvas画布填充了图片
        return 'data:image/png;base64,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'
    },
    style: {},
    setAttribute: function (p, v) {
        this[p] = v
    },
    getAttributeNames: function (p) {
        //console.log(p);
        return this[p]
    }
}
CanvasRenderingContext2D = {
    fillRect: function () {
    },
    fillText: function () {
    }, style: {}
}
document = {
    cookie: "",
    documentElement: {},
    hidden: false,
    webkitHidden: false,
    wasDiscarded: false,
    addEventListener: function () {
    },
    getElementById: function (tag) {
        if (tag.indexOf('_') !== -1) {
            return null
        } else {
            return {id: tag}
        }
    },
    createElement: function (tag) {
        if (tag === 'canvas') {
            return canvas;
        } else {
            return {
                targetName: tag,
                style: {
                    'text-rendering': '',
                    resize: '',
                    'text-align-last': '',
                },firstChild:location
            }
        }
    },
    location: {
      "ancestorOrigins":{},
      "href":"https://jobs.51job.com/beijing/123284714.html?s=sou_sou_soulb&t=0_0"
      ,"origin":"https://jobs.51job.com"
      ,"protocol":"https:",
      "host":"jobs.51job.com",
      "hostname":"jobs.51job.com",
      "port":"",
      "pathname":"/beijing/123284714.html",
      "search":"?s=sou_sou_soulb&t=0_0",
      "hash":"",

    },referrer:''
}
navigator = {
    cookieEnabled: true,
    hardwareConcurrency: 8,
    language: "zh-CN",
    appName: "Netscape",
    product: "Gecko",
    productSub: "20030107",
    appCodeName: "Mozilla",
    languages: ['zh-CN', 'zh', 'en'],
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    userAgentData: {
        brands: [
            {brand: ".Not/A)Brand", version: "99"},
            {brand: "Chromium", version: "103"},
            {brand: "Google Chrome", version: "103"},
        ],
        mobile: false,
        platform: 'Windows'
    },
    platform: "Win32",
    webdriver: false,
    plugins: [{"name": "PDF Viewer", "filename": "internal-pdf-viewer"}, {
        "name": "Chrome PDF Viewer",
        "filename": "internal-pdf-viewer"
    }, {"name": "Chromium PDF Viewer", "filename": "internal-pdf-viewer"}, {
        "name": "Microsoft Edge PDF Viewer",
        "filename": "internal-pdf-viewer"
    }, {"name": "WebKit built-in PDF", "filename": "internal-pdf-viewer"}],
    toString: function () {
        return '[object Navigator]'
    }
}
my_func = Function.prototype.toString;
Function.prototype.toString = function () {
// console.log(arguments);
    let val = my_func.apply(this, arguments);
    if (val.indexOf('[object') !== -1) {
        return val
    } else {
        return val.replace(/\s+/g, '')
    }
}
document.toString = function () {
    return '[object HTMLDocument]'
}
canvas = hook(canvas)
window = global;
window.performance = {
    eventCounts: {size: 36},
    memory: {
        jsHeapSizeLimit: 4294705152,
        totalJSHeapSize: 42920529,
        usedJSHeapSize: 37143009,
    },
    navigation: {
        redirectCount: 0,
        type: 1
    }, onresourcetimingbufferfull: null,
    timeOrigin: 1658801530085.4,
    timing: {
        connectEnd: 1658801530088,
        connectStart: 1658801530088,
        domComplete: 1658824130162,
        domContentLoadedEventEnd: 1658801530941,
        domContentLoadedEventStart: 1658801530935,
        domInteractive: 1658801530935,
        domLoading: 1658801530197,
        domainLookupEnd: 1658801530088,
        domainLookupStart: 1658801530088,
        fetchStart: 1658801530088,
        loadEventEnd: 1658824130173,
        loadEventStart: 1658824130162,
        navigationStart: 1658801530085,
        redirectEnd: 0,
        redirectStart: 0,
        requestStart: 1658801530097,
        responseEnd: 1658801530180,
        responseStart: 1658801530152,
        secureConnectionStart: 0,
        unloadEventEnd: 1658801530187,
        unloadEventStart: 1658801530187,
    }
}
window.origin = 'https://search.51job.com'
window.location = location = document.location;
window.PerformanceTiming = function () {
}
window.Intl = {
    "getCanonicalLocales": function () {
    },
    "supportedValuesOf": function () {
    },
    "DateTimeFormat": function () {
    },
    "NumberFormat": function () {
    },
    "Collator": function () {
    },
    "v8BreakIterator": function () {
    },
    "PluralRules": function () {
    },
    "RelativeTimeFormat": function () {
    },
    "ListFormat": function () {
    },
    "Locale": function () {
    },
    "DisplayNames": function () {
    },
    "Segmenter": function () {
    },
    toString: function () {
        return '[object Intl]'
    },
}
window.PerformanceServerTiming = function () {
}
window.HTMLDocument = function () {
}
window.HTMLMediaElement = function () {
}
window.Touch = function () {
}
window.RTCPeerConnection = function () {
}
window.Element = function () {
}
window.Bluetooth = function () {
}
window.PointerEvent = function () {
}
window.PointerEvent.prototype.getCoalescedEvents = function () {
}
window.webkitRTCPeerConnection = function () {
}
window.BluetoothDevice = function () {
}
window.BluetoothUUID = function () {
}
window.OfflineAudioContext = function () {
    this.createOscillator = function () {
        return {
            frequency: {
                setValueAtTime: function () {
                }
            },
            connect: function () {
            },
            start: function () {
            },
        }
    },
        this.createDynamicsCompressor = function () {
            return {
                threshold: {
                    setValueAtTime: function () {
                    },
                },
                setValueAtTime: function () {
                },
                knee: {
                    setValueAtTime: function () {
                    },
                },
                ratio: {
                    setValueAtTime: function () {
                    },
                },
                reduction: {
                    setValueAtTime: function () {
                    },
                },
                attack: {
                    setValueAtTime: function () {
                    },
                },
                release: {
                    setValueAtTime: function () {
                    },
                },
                connect: function () {
                },
            }
        },
        this.startRendering = function () {
        },
        this.currentTime = new Date().getTime()
}
window.screen = {
    availHeight: 680,
    availLeft: 0,
    availTop: 0,
    availWidth: 1280,
    colorDepth: 24,
    height: 720,
    isExtended: false,
    onchange: null,
    orientation: {angle: 0, type: 'landscape-primary', onchange: null},
    pixelDepth: 24,
    width: 1280,
}
window.Buffer = undefined
window.outerWidth = 1280
window.outerHeight = 680
window.innerHeight = 641
window.innerWidth = 1422
window.screenX = 0
window.screenY = 0
window.screenTop = 0
window.screenLeft = 0
window.history = {
    pushState: function () {
    },
    replaceState: function () {
    },
    length: 11,
    scrollRestoration: "auto",
    state: {key: '345432.500'}
}
window.navigator = navigator
window.isSecureContext = true
window.toString = function () {
    return '[object Window]'
}
window = new Proxy(window, {
    get: function (o, p) {
        if (p === "Symbol") {
            return undefined
        } else {
            return o[p]
        }
    }
})
window.self = window
global = undefined


get_url = function (base_url) {
  location.href = base_url
  location.pathname = location.href.match(/\.com(.*?)\?/i)[1]

  var _0x5c7e9e = function (_0x26f6bc) {
    var _0x464f9 = document["createElement"]("div"),
        _0x3d4932;

    _0x464f9["innerHTML"] = "<a></a>";
    _0x464f9["firstChild"]["href"] = _0x26f6bc;
    _0x464f9["innerHTML"] = _0x464f9["innerHTML"];
    _0x3d4932 = _0x464f9["firstChild"];
    _0x3d4932["href"] = _0x464f9["firstChild"]["href"];
    return {
      'protocol': _0x3d4932["protocol"],
      'host': _0x3d4932["host"],
      'hostname': _0x3d4932["hostname"],
      'port': _0x3d4932["port"],
      'pathname': _0x3d4932["pathname"]["substr"](0x0, 0x1) === '/' ? _0x3d4932["pathname"] : '/' + _0x3d4932["pathname"],
      'search': _0x3d4932["search"],
      'hash': _0x3d4932["hash"],
      'original': _0x3d4932["href"]
    };
  };

  var _0x4f8119 = function (_0x1ae36f) {
    if ("duCiQ" === "glhAW") {
      _0xf0f009 = 0x0;

      _0x1151bc["push"](_0x425b02(_0x5d98f7));

      _0xb45f98 = 0x0;
    } else {
      if (_0x1ae36f["charAt"](0x0) != '?') {
        if ("MOvsy" !== "MOvsy") {
          _0xac0760["keys"](_0x511f72)["forEach"](function (_0x465e33) {
            var _0x50d04b = _0x2f3969["document"][_0x465e33];

            if (_0x50d04b && _0x50d04b["hasOwnProperty"]("idPrefix_") && _0x50d04b["hasOwnProperty"]("cache_") && _0x50d04b["hasOwnProperty"]("nextId_")) {
              _0x3a5566 = 0x1;
            }
          });
        } else {
          return {};
        }
      }

      var _0x4d90a1 = {};

      var _0x276e74 = _0x1ae36f["substr"](0x1)["split"]('&');

      for (var _0x463ea2 = 0x0; _0x463ea2 < _0x276e74["length"]; _0x463ea2++) {
        var _0xcb29f = _0x276e74[_0x463ea2]["split"]('=');

        try {
          if ("vDNbC" !== "mdaPm") {
            _0x4d90a1[decodeURIComponent(_0xcb29f[0x0])] = decodeURIComponent(_0xcb29f[0x1] || '');
          } else {
            _0x34f702 = _0x12f4e9 << 0x1;

            if (_0x57b1ad == _0x323db1 - 0x1) {
              _0x5aae5d = 0x0;

              _0x37ed02["push"](_0x421bb0(_0x15a43b));

              _0x361c15 = 0x0;
            } else {
              _0xc55bc7++;
            }
          }
        } catch (_0x25dcf0) {
          _0x4d90a1[decodeURIComponent(_0xcb29f[0x0] && _0xcb29f[0x0]["replace"](/\%/g, "%25"))] = decodeURIComponent(_0xcb29f[0x1] && _0xcb29f[0x1]["replace"](/\%/g, "%25") || '');
        }
      }

      return _0x4d90a1;
    }
  };

  var _0x3bd005 = function (_0xd9d887, _0x418277) {
    var _0x340c2c = _0x4f8119(_0xd9d887);

    var _0x163f61 = '?';

    for (var _0x3649db in _0x418277) {
      _0x340c2c[_0x3649db] = _0x418277[_0x3649db];
    }

    for (var _0x3649db in _0x340c2c) {
      if ("sJjNJ" === "BHjWW") {
        _0x414220 = 0x0;

        _0x11d047["push"](_0x3b2e18(_0x2d2572));

        _0x3a198e = 0x0;
      } else {
        _0x163f61 += encodeURIComponent(_0x3649db) + '=' + encodeURIComponent(_0x340c2c[_0x3649db]) + '&';
      }
    }

    _0x163f61 = _0x163f61["substr"](0x0, _0x163f61["length"] - 0x1);
    return _0x163f61;
  };

  var _0x4643db = function (_0x1129d6, _0x44432b) {
    if ("DPnTn" === "lFfMh") {
      _0x3b9d96 = _0x839b46 << 0x1 | _0x251586 & 0x1;

      if (_0xa9f0da == _0x1d93a5 - 0x1) {
        _0x27401f = 0x0;

        _0x36ea6c["push"](_0x31cd45(_0x17e138));

        _0xd9b36 = 0x0;
      } else {
        _0x10d8ed++;
      }

      _0x20f6eb = _0x3e95a9 >> 0x1;
    } else {
      var _0x243caf = _0x1129d6["indexOf"](_0x44432b);

      if (_0x243caf < 0x0 || _0x1129d6[_0x243caf + _0x44432b["length"]] != '=') {
        return _0x1129d6;
      }

      var _0x42334f = _0x1129d6["indexOf"]('&', _0x243caf);

      var _0x1fcb26 = '';

      if (_0x42334f == -0x1) {
        _0x1fcb26 = _0x1129d6["substring"](0x0, _0x243caf);
      } else {
        _0x1fcb26 = _0x1129d6["substring"](0x0, _0x243caf) + _0x1129d6["substring"](_0x42334f + 0x1);
      }

      if (_0x1fcb26[_0x1fcb26["length"] - 0x1] == '?' || _0x1fcb26[_0x1fcb26["length"] - 0x1] == '&') {
        _0x1fcb26 = _0x1fcb26["substring"](0x0, _0x1fcb26["length"] - 0x1);
      }

      return _0x1fcb26;
    }
  };

  var _0x48736b = function (_0x375b7d) {
    return _0x375b7d["protocol"] + '//' + _0x375b7d["host"] + _0x375b7d["pathname"] + _0x375b7d["search"] + _0x375b7d["hash"];
  };

  var _0x56d97c = function (_0x8df421) {
    if ("XCHet" !== "XCHet") {
      var _0x343167 = _0x229eef["document"][_0x18eedd];

      if (_0x343167 && _0x343167["hasOwnProperty"]("idPrefix_") && _0x343167["hasOwnProperty"]("cache_") && _0x343167["hasOwnProperty"]("nextId_")) {
        _0x5e911d = 0x1;
      }
    } else {
      if (_0x8df421 == null) return '';
      var _0x1a190e = String["fromCharCode"];
      var _0x3219b6 = "DGi0YA7BemWnQjCl4+bR3f8SKIF9tUz/xhr2oEOgPpac=61ZqwTudLkM5vHyNXsVJ";
      var _0x33fb4f = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-$";
      var _0x5d342f = {};
      var _0xc885ae = 0x6;

      var _0x1637ab = function (_0x329955) {
        if ("eEKjo" === "QrDfB") {
          _0x2be31f = 0x1;
        } else {
          return _0x3219b6["charAt"](_0x329955);
        }
      };

      if (_0x8df421 == null) return '';

      var _0x2ba560,
          _0x1a3125,
          _0x56a845 = {},
          _0x568d8a = {},
          _0x17ecc2 = '',
          _0x4b03fb = '',
          _0x127752 = '',
          _0x55a847 = 0x2,
          _0x48b33e = 0x3,
          _0x318c3 = 0x2,
          _0x24e447 = [],
          _0x841ee6 = 0x0,
          _0x25adf9 = 0x0,
          _0x4afbc9;

      for (_0x4afbc9 = 0x0; _0x4afbc9 < _0x8df421["length"]; _0x4afbc9 += 0x1) {
        if ("EDNzU" !== "CMeWZ") {
          _0x17ecc2 = _0x8df421["charAt"](_0x4afbc9);

          if (!Object["prototype"]["hasOwnProperty"]["call"](_0x56a845, _0x17ecc2)) {
            if ("bBkTv" === "bBkTv") {
              _0x56a845[_0x17ecc2] = _0x48b33e++;
              _0x568d8a[_0x17ecc2] = !![];
            } else {
              _0x586061["search"] = _0x138f86(_0x32aa91["search"], {
                'alichlgref': _0x35fc62["referrer"]
              });
            }
          }

          _0x4b03fb = _0x127752 + _0x17ecc2;

          if (Object["prototype"]["hasOwnProperty"]["call"](_0x56a845, _0x4b03fb)) {
            _0x127752 = _0x4b03fb;
          } else {
            if ("SEcKB" === "TwzUG") {
              _0x4f3fe7++;
            } else {
              if (Object["prototype"]["hasOwnProperty"]["call"](_0x568d8a, _0x127752)) {
                if ("ylTCc" !== "ylTCc") {
                  _0x3579ce = _0x7a15ac << 0x1 | _0x596d29 & 0x1;

                  if (_0x5e99c6 == _0x377b0a - 0x1) {
                    _0x44fe7a = 0x0;

                    _0x1ea166["push"](_0x2bf671(_0x57ff55));

                    _0x5b7cb8 = 0x0;
                  } else {
                    _0x5ef9d9++;
                  }

                  _0x29a523 = _0x1f9864 >> 0x1;
                } else {
                  if (_0x127752["charCodeAt"](0x0) < 0x100) {
                    for (_0x2ba560 = 0x0; _0x2ba560 < _0x318c3; _0x2ba560++) {
                      _0x841ee6 = _0x841ee6 << 0x1;

                      if (_0x25adf9 == _0xc885ae - 0x1) {
                        _0x25adf9 = 0x0;

                        _0x24e447["push"](_0x1637ab(_0x841ee6));

                        _0x841ee6 = 0x0;
                      } else {
                        _0x25adf9++;
                      }
                    }

                    _0x1a3125 = _0x127752["charCodeAt"](0x0);

                    for (_0x2ba560 = 0x0; _0x2ba560 < 0x8; _0x2ba560++) {
                      _0x841ee6 = _0x841ee6 << 0x1 | _0x1a3125 & 0x1;

                      if (_0x25adf9 == _0xc885ae - 0x1) {
                        _0x25adf9 = 0x0;

                        _0x24e447["push"](_0x1637ab(_0x841ee6));

                        _0x841ee6 = 0x0;
                      } else {
                        _0x25adf9++;
                      }

                      _0x1a3125 = _0x1a3125 >> 0x1;
                    }
                  } else {
                    if ("Mbxao" !== "Mbxao") {
                      _0x1acac8 = 0x0;

                      _0x53d53e["push"](_0x49d82f(_0x16659d));

                      _0x59824c = 0x0;
                    } else {
                      _0x1a3125 = 0x1;

                      for (_0x2ba560 = 0x0; _0x2ba560 < _0x318c3; _0x2ba560++) {
                        if ("tGGyM" === "NrXkr") {
                          _0x4de593++;
                        } else {
                          _0x841ee6 = _0x841ee6 << 0x1 | _0x1a3125;

                          if (_0x25adf9 == _0xc885ae - 0x1) {
                            _0x25adf9 = 0x0;

                            _0x24e447["push"](_0x1637ab(_0x841ee6));

                            _0x841ee6 = 0x0;
                          } else {
                            if ("fQrHu" === "fQrHu") {
                              _0x25adf9++;
                            } else {
                              if (_0x416bb0) {
                                return 0x1;
                              } else {
                                return 0x0;
                              }
                            }
                          }

                          _0x1a3125 = 0x0;
                        }
                      }

                      _0x1a3125 = _0x127752["charCodeAt"](0x0);

                      for (_0x2ba560 = 0x0; _0x2ba560 < 0x10; _0x2ba560++) {
                        if ("cVNch" === "cVNch") {
                          _0x841ee6 = _0x841ee6 << 0x1 | _0x1a3125 & 0x1;

                          if (_0x25adf9 == _0xc885ae - 0x1) {
                            _0x25adf9 = 0x0;

                            _0x24e447["push"](_0x1637ab(_0x841ee6));

                            _0x841ee6 = 0x0;
                          } else {
                            if ("kZKPa" === "elIvN") {
                              _0x3db489++;
                            } else {
                              _0x25adf9++;
                            }
                          }

                          _0x1a3125 = _0x1a3125 >> 0x1;
                        } else {
                          _0x4f29da++;
                          if (_0x503ad6 == 0x2) return '';
                        }
                      }
                    }
                  }

                  _0x55a847--;

                  if (_0x55a847 == 0x0) {
                    if ("tOOOh" === "tOOOh") {
                      _0x55a847 = Math["pow"](0x2, _0x318c3);
                      _0x318c3++;
                    } else {
                      _0x37b477 = _0x5d3ab9[_0xc17916];

                      for (_0x4ca415 = 0x0; _0x32bf09 < _0x9f6d5e; _0x43b89++) {
                        _0x3f5dd9 = _0x525588 << 0x1 | _0x49d704 & 0x1;

                        if (_0x41a525 == _0x1a9092 - 0x1) {
                          _0x529efc = 0x0;

                          _0x5f434a["push"](_0x3deab8(_0x11b2a6));

                          _0x30cfcf = 0x0;
                        } else {
                          _0x10a129++;
                        }

                        _0x187e07 = _0x4ffbd3 >> 0x1;
                      }
                    }
                  }

                  delete _0x568d8a[_0x127752];
                }
              } else {
                if ("XDIft" !== "xtevT") {
                  _0x1a3125 = _0x56a845[_0x127752];

                  for (_0x2ba560 = 0x0; _0x2ba560 < _0x318c3; _0x2ba560++) {
                    _0x841ee6 = _0x841ee6 << 0x1 | _0x1a3125 & 0x1;

                    if (_0x25adf9 == _0xc885ae - 0x1) {
                      _0x25adf9 = 0x0;

                      _0x24e447["push"](_0x1637ab(_0x841ee6));

                      _0x841ee6 = 0x0;
                    } else {
                      _0x25adf9++;
                    }

                    _0x1a3125 = _0x1a3125 >> 0x1;
                  }
                } else {
                  _0x2b603a++;
                }
              }

              _0x55a847--;

              if (_0x55a847 == 0x0) {
                if ("FVAgE" !== "XqucF") {
                  _0x55a847 = Math["pow"](0x2, _0x318c3);
                  _0x318c3++;
                } else {
                  _0x13cc4b = _0x1de9b7[_0x3c5ed9];

                  for (_0x31f564 = 0x0; _0x434349 < _0x266852; _0x4318eb++) {
                    _0x1184ef = _0xc95779 << 0x1 | _0x56c1eb & 0x1;

                    if (_0x154348 == _0x43bae - 0x1) {
                      _0x174ff2 = 0x0;

                      _0x310d0e["push"](_0x3c6b85(_0x8d2a17));

                      _0x1cf61a = 0x0;
                    } else {
                      _0x39dc8f++;
                    }

                    _0x9148e4 = _0x49c5da >> 0x1;
                  }
                }
              }

              _0x56a845[_0x4b03fb] = _0x48b33e++;
              _0x127752 = String(_0x17ecc2);
            }
          }
        } else {
          _0x18923a++;
        }
      }

      if (_0x127752 !== '') {
        if (Object["prototype"]["hasOwnProperty"]["call"](_0x568d8a, _0x127752)) {
          if ("pwjFI" !== "pwjFI") {
            _0x4f2452 = 0x0;

            _0x4d1bc3["push"](_0xaafa6d(_0x4c906d));

            _0x443c56 = 0x0;
          } else {
            if (_0x127752["charCodeAt"](0x0) < 0x100) {
              if ("pnZzb" !== "SolBZ") {
                for (_0x2ba560 = 0x0; _0x2ba560 < _0x318c3; _0x2ba560++) {
                  _0x841ee6 = _0x841ee6 << 0x1;

                  if (_0x25adf9 == _0xc885ae - 0x1) {
                    if ("lBGsP" === "ojwnB") {
                      return 0x1;
                    } else {
                      _0x25adf9 = 0x0;

                      _0x24e447["push"](_0x1637ab(_0x841ee6));

                      _0x841ee6 = 0x0;
                    }
                  } else {
                    if ("WpDRL" === "FQojr") {
                      _0x204835 = _0x51e5e0;
                    } else {
                      _0x25adf9++;
                    }
                  }
                }

                _0x1a3125 = _0x127752["charCodeAt"](0x0);

                for (_0x2ba560 = 0x0; _0x2ba560 < 0x8; _0x2ba560++) {
                  _0x841ee6 = _0x841ee6 << 0x1 | _0x1a3125 & 0x1;

                  if (_0x25adf9 == _0xc885ae - 0x1) {
                    _0x25adf9 = 0x0;

                    _0x24e447["push"](_0x1637ab(_0x841ee6));

                    _0x841ee6 = 0x0;
                  } else {
                    if ("vIIre" !== "OXJUT") {
                      _0x25adf9++;
                    } else {
                      _0x44559d++;
                    }
                  }

                  _0x1a3125 = _0x1a3125 >> 0x1;
                }
              } else {
                return 0x0;
              }
            } else {
              if ("CCOte" !== "IemYU") {
                _0x1a3125 = 0x1;

                for (_0x2ba560 = 0x0; _0x2ba560 < _0x318c3; _0x2ba560++) {
                  if ("wTzwI" !== "wTzwI") {
                    _0x1d2d3b = _0x3c6db7["substring"](0x0, _0x9418d6);
                  } else {
                    _0x841ee6 = _0x841ee6 << 0x1 | _0x1a3125;

                    if (_0x25adf9 == _0xc885ae - 0x1) {
                      _0x25adf9 = 0x0;

                      _0x24e447["push"](_0x1637ab(_0x841ee6));

                      _0x841ee6 = 0x0;
                    } else {
                      _0x25adf9++;
                    }

                    _0x1a3125 = 0x0;
                  }
                }

                _0x1a3125 = _0x127752["charCodeAt"](0x0);

                for (_0x2ba560 = 0x0; _0x2ba560 < 0x10; _0x2ba560++) {
                  if ("izTop" !== "izTop") {
                    _0x3de1dd++;
                  } else {
                    _0x841ee6 = _0x841ee6 << 0x1 | _0x1a3125 & 0x1;

                    if (_0x25adf9 == _0xc885ae - 0x1) {
                      _0x25adf9 = 0x0;

                      _0x24e447["push"](_0x1637ab(_0x841ee6));

                      _0x841ee6 = 0x0;
                    } else {
                      _0x25adf9++;
                    }

                    _0x1a3125 = _0x1a3125 >> 0x1;
                  }
                }
              } else {
                _0x37f5c3 = _0x20ba01 << 0x1 | _0x52f125;

                if (_0x422e93 == _0x306c4f - 0x1) {
                  _0x2b59f7 = 0x0;

                  _0x5c18ea["push"](_0x17441d(_0x1d334e));

                  _0x503f27 = 0x0;
                } else {
                  _0x345dd9++;
                }

                _0x53381c = 0x0;
              }
            }

            _0x55a847--;

            if (_0x55a847 == 0x0) {
              _0x55a847 = Math["pow"](0x2, _0x318c3);
              _0x318c3++;
            }

            delete _0x568d8a[_0x127752];
          }
        } else {
          if ("XhWEG" !== "JaiOO") {
            _0x1a3125 = _0x56a845[_0x127752];

            for (_0x2ba560 = 0x0; _0x2ba560 < _0x318c3; _0x2ba560++) {
              _0x841ee6 = _0x841ee6 << 0x1 | _0x1a3125 & 0x1;

              if (_0x25adf9 == _0xc885ae - 0x1) {
                _0x25adf9 = 0x0;

                _0x24e447["push"](_0x1637ab(_0x841ee6));

                _0x841ee6 = 0x0;
              } else {
                if ("AHqWc" === "JMWpW") {
                  _0x545b2e = _0x4743e << 0x1 | _0x449caa & 0x1;

                  if (_0x39e7a0 == _0x5a30cb - 0x1) {
                    _0x50de0e = 0x0;

                    _0x25ac9d["push"](_0x4df853(_0x157f91));

                    _0x8b84ed = 0x0;
                  } else {
                    _0x3b77c1++;
                  }

                  _0x4636d9 = _0x4147b3 >> 0x1;
                } else {
                  _0x25adf9++;
                }
              }

              _0x1a3125 = _0x1a3125 >> 0x1;
            }
          } else {
            return _0x15f98b;
          }
        }

        _0x55a847--;

        if (_0x55a847 == 0x0) {
          _0x55a847 = Math["pow"](0x2, _0x318c3);
          _0x318c3++;
        }
      }

      _0x1a3125 = 0x2;

      for (_0x2ba560 = 0x0; _0x2ba560 < _0x318c3; _0x2ba560++) {
        if ("HOAug" !== "HOAug") {
          var _0x95ab9 = _0x15ffa9[_0x594232]["split"]('=');

          try {
            _0x1709fd[_0x458358(_0x95ab9[0x0])] = _0x76329c(_0x95ab9[0x1] || '');
          } catch (_0xe917bd) {
            _0x88e515[_0x8aea66(_0x95ab9[0x0] && _0x95ab9[0x0]["replace"](/\%/g, "%25"))] = _0x29dfff(_0x95ab9[0x1] && _0x95ab9[0x1]["replace"](/\%/g, "%25") || '');
          }
        } else {
          _0x841ee6 = _0x841ee6 << 0x1 | _0x1a3125 & 0x1;

          if (_0x25adf9 == _0xc885ae - 0x1) {
            if ("Licex" !== "Licex") {
              _0x9c19b7++;
            } else {
              _0x25adf9 = 0x0;

              _0x24e447["push"](_0x1637ab(_0x841ee6));

              _0x841ee6 = 0x0;
            }
          } else {
            if ("yEKjY" === "LipPO") {
              _0x5a1b13 = 0x0;

              _0x26db1e["push"](_0x32e446(_0x23bb46));

              _0x19eaec = 0x0;
            } else {
              _0x25adf9++;
            }
          }

          _0x1a3125 = _0x1a3125 >> 0x1;
        }
      }

      while (!![]) {
        _0x841ee6 = _0x841ee6 << 0x1;

        if (_0x25adf9 == _0xc885ae - 0x1) {
          if ("FYJtP" !== "vxULq") {
            _0x24e447["push"](_0x1637ab(_0x841ee6));

            break;
          } else {
            _0x5db311 = _0x21dec4["documentElement"]["getAttribute"] && _0x1fb946["documentElement"]["getAttribute"]("webdriver");
          }
        } else _0x25adf9++;
      }

      return _0x24e447["join"]('');
    }
  };


  var _0x350f61 = window;
  var _0x43cf25 = document;

  function _0x4ff6e9(_0x676b3d) {
    if (_0x676b3d) {
      if ("UlzLc" !== "zScQE") {
        return 0x1;
      } else {
        _0x1705b6++;
      }
    } else {
      if ("zpYzt" === "kqDdd") {
        _0x59ad60 = _0x4cbc94["original"]["charCodeAt"](_0x11ce3c);
        _0x2bf8d0 = (_0x36b4d2 << 0x7) - _0x4f6dd3 + 0x18e + _0xff0d0c;
        _0x18f00b |= 0x0;
      } else {
        return 0x0;
      }
    }
  }

  var _0x3e3064 = '';

  try {
    if ("Owuvn" === "wofIO") {
      _0x4e6998 = 0x0;

      _0x1423c1["push"](_0x33b359(_0x47e5e4));

      _0x4bbb7c = 0x0;
    } else {
      _0x3e3064 = _0x43cf25["documentElement"]["getAttribute"] && _0x43cf25["documentElement"]["getAttribute"]("webdriver");
    }
  } catch (_0x439634) {}

  var _0x4a57d3 = 0x0;

  if (_0x350f61["hasOwnProperty"]) {
    if ("JaYlf" === "MhTzj") {
      _0x3ec74e = _0x189a87["pow"](0x2, _0x1fb243);
      _0x5e0093++;
    } else {
      Object["keys"](_0x43cf25)["forEach"](function (_0x2fb349) {
        var _0x434fbd = _0x350f61["document"][_0x2fb349];

        if (_0x434fbd && _0x434fbd["hasOwnProperty"]("idPrefix_") && _0x434fbd["hasOwnProperty"]("cache_") && _0x434fbd["hasOwnProperty"]("nextId_")) {
          if ("qxNiz" !== "oHDfY") {
            _0x4a57d3 = 0x1;
          } else {
            _0x66448f = _0x162cc9 << 0x1 | _0x1729c6 & 0x1;

            if (_0x16d698 == _0x2e8207 - 0x1) {
              _0x41d308 = 0x0;

              _0x2a9050["push"](_0x511fe6(_0x1a5f7e));

              _0x57bddc = 0x0;
            } else {
              _0x3cc644++;
            }

            _0x513b17 = _0x46c5e5 >> 0x1;
          }
        }
      });
    }
  }

  var _0x383ee0 = new Date();

  var _0x465be6 = 0x0;

  _0x383ee0["toString"] = function () {
    _0x465be6++;
    if (_0x465be6 == 0x2) return '';
  };



  var _0x4d6ae3 = 0;

  var _0x218d3d = 0x0;
  _0x218d3d |= _0x4ff6e9(_0x4d6ae3) << 0x0;
  _0x218d3d |= _0x4ff6e9(navigator["webdriver"]) << 0x1;
  _0x218d3d |= _0x4ff6e9(_0x4a57d3) << 0x2;
  _0x218d3d |= _0x4ff6e9(_0x350f61["_phantom"]) << 0x3;
  _0x218d3d |= _0x4ff6e9(_0x350f61["callPhantom"]) << 0x4;
  _0x218d3d |= _0x4ff6e9(_0x350f61["phantom"]) << 0x5;
  _0x218d3d |= _0x4ff6e9(_0x350f61["spawn"]) << 0x6;
  _0x218d3d |= _0x4ff6e9(_0x350f61["emit"]) << 0x7;
  _0x218d3d |= _0x4ff6e9(_0x3e3064) << 0x8;
  _0x218d3d |= _0x4ff6e9(_0x350f61["Buffer"]) << 0x9;
  _0x218d3d |= _0x4ff6e9(_0x350f61["domAutomation"]) << 0xa;
  _0x218d3d |= _0x4ff6e9(_0x350f61["webdriver"]) << 0xb;
  _0x218d3d |= _0x4ff6e9(_0x43cf25["__webdriver_script_fn"]) << 0xc;
  _0x218d3d |= _0x4ff6e9(_0x350f61["fxdriver_id"]) << 0xd;
  _0x218d3d |= _0x4ff6e9(_0x350f61["__fxdriver_unwrapped"]) << 0xe;
  _0x218d3d |= _0x4ff6e9(_0x350f61["ClientUtils"]) << 0xf;

  var _0x1117c9 = _0x5c7e9e(document["location"]["href"]);

  var _0x420dc7 = 0x0;

  for (var _0x465be6 = 0x0; _0x465be6 < _0x1117c9["host"]["length"]; _0x465be6++) {
    if ("fHEdp" === "ytRLg") {
      _0x432b52 = 0x0;

      _0x3453ae["push"](_0x5bc9b4(_0x2443de));

      _0x9ba582 = 0x0;
    } else {
      _0x420dc7 = _0x420dc7 + _0x1117c9["host"][_0x465be6]["charCodeAt"]();
    }
  }

  var _0x3a7bdd = ["type__", "refer__", "ipcity__", "md5__", "decode__", "encode__", "time__", "timestamp__", "type__"];

  var _0x3e621b = _0x3a7bdd[_0x420dc7 % _0x3a7bdd["length"]] + _0x420dc7 % 0x2710;

  _0x1117c9["search"] = _0x4643db(_0x1117c9["search"], _0x3e621b);
  _0x1117c9["original"] = _0x4643db(_0x1117c9["original"], _0x3e621b);
  _0x1117c9["search"] = _0x4643db(_0x1117c9["search"], "alichlgref");
  _0x1117c9["original"] = _0x4643db(_0x1117c9["original"], "alichlgref");
  var _0x318558 = 0x0;

  var _0x465be6, _0x44becc;

  for (_0x465be6 = 0x0; _0x465be6 < _0x1117c9["original"]["length"]; _0x465be6++) {
    _0x44becc = _0x1117c9["original"]["charCodeAt"](_0x465be6);
    _0x318558 = (_0x318558 << 0x7) - _0x318558 + 0x18e + _0x44becc;
    _0x318558 |= 0x0;
  }

  var _0x30f62c = _0x56d97c(_0x318558 + '|' + _0x218d3d + '|' + (new Date()["getTime"]() + ''));

  var _0x3baf44 = {};
  _0x3baf44[_0x3e621b] = _0x30f62c;
  _0x1117c9["search"] = _0x3bd005(_0x1117c9["search"], _0x3baf44);

  if (document["referrer"] != '') {
    if ("ZihLF" === "PXCSY") {
      _0x58e1aa = _0x3187df["pow"](0x2, _0x4672ff);
      _0x56ace8++;
    } else {
      _0x1117c9["search"] = _0x3bd005(_0x1117c9["search"], {
        'alichlgref': document["referrer"]
      });
    }
  }

  var _0x5e2296 = _0x48736b(_0x1117c9);
  // console.log(_0x5e2296)
  return _0x5e2296
};

// console.log(get_url('https://jobs.51job.com/beijing/123284714.html?s=sou_sou_soulb&t=0_0'))