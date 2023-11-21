!function() {
    var e = {
        504: function(e) {
            "use strict";
            function t(e, t) {
                return Object.prototype.hasOwnProperty.call(e, t)
            }
            e.exports = function(e, n, r, o) {
                n = n || "&",
                r = r || "=";
                var i = {};
                if ("string" != typeof e || 0 === e.length)
                    return i;
                var a = /\+/g;
                e = e.split(n);
                var c = 1e3;
                o && "number" == typeof o.maxKeys && (c = o.maxKeys);
                var u = e.length;
                c > 0 && u > c && (u = c);
                for (var s = 0; s < u; ++s) {
                    var f, d, l, p, g = e[s].replace(a, "%20"), v = g.indexOf(r);
                    v >= 0 ? (f = g.substr(0, v),
                    d = g.substr(v + 1)) : (f = g,
                    d = ""),
                    l = decodeURIComponent(f),
                    p = decodeURIComponent(d),
                    t(i, l) ? Array.isArray(i[l]) ? i[l].push(p) : i[l] = [i[l], p] : i[l] = p
                }
                return i
            }
        },
        7950: function(e) {
            "use strict";
            var t = function(e) {
                switch (typeof e) {
                case "string":
                    return e;
                case "boolean":
                    return e ? "true" : "false";
                case "number":
                    return isFinite(e) ? e : "";
                default:
                    return ""
                }
            };
            e.exports = function(e, n, r, o) {
                return n = n || "&",
                r = r || "=",
                null === e && (e = void 0),
                "object" == typeof e ? Object.keys(e).map((function(o) {
                    var i = encodeURIComponent(t(o)) + r;
                    return Array.isArray(e[o]) ? e[o].map((function(e) {
                        return i + encodeURIComponent(t(e))
                    }
                    )).join(n) : i + encodeURIComponent(t(e[o]))
                }
                )).filter(Boolean).join(n) : o ? encodeURIComponent(t(o)) + r + encodeURIComponent(t(e)) : ""
            }
        },
        2396: function(e, t, n) {
            "use strict";
            t.parse = n(504),
            n(7950)
        },
        17: function(e, t, n) {
            n(2966),
            e.exports = n(3142).Date.now
        },
        7606: function(e, t, n) {
            var r = n(3142)
              , o = r.JSON || (r.JSON = {
                stringify: JSON.stringify
            });
            e.exports = function(e) {
                return o.stringify.apply(o, arguments)
            }
        },
        1225: function(e, t, n) {
            n(6285),
            e.exports = n(3142).Object.assign
        },
        5339: function(e, t, n) {
            n(3706);
            var r = n(3142).Object;
            e.exports = function(e, t, n) {
                return r.defineProperty(e, t, n)
            }
        },
        2034: function(e, t, n) {
            n(3176),
            e.exports = n(3142).Object.freeze
        },
        4799: function(e, t, n) {
            n(7462),
            e.exports = n(3142).Object.keys
        },
        3749: function(e) {
            e.exports = function(e) {
                if ("function" != typeof e)
                    throw TypeError(e + " is not a function!");
                return e
            }
        },
        8891: function(e, t, n) {
            var r = n(2799);
            e.exports = function(e) {
                if (!r(e))
                    throw TypeError(e + " is not an object!");
                return e
            }
        },
        4351: function(e, t, n) {
            var r = n(4188)
              , o = n(2642)
              , i = n(2360);
            e.exports = function(e) {
                return function(t, n, a) {
                    var c, u = r(t), s = o(u.length), f = i(a, s);
                    if (e && n != n) {
                        for (; s > f; )
                            if ((c = u[f++]) != c)
                                return !0
                    } else
                        for (; s > f; f++)
                            if ((e || f in u) && u[f] === n)
                                return e || f || 0;
                    return !e && -1
                }
            }
        },
        9606: function(e) {
            var t = {}.toString;
            e.exports = function(e) {
                return t.call(e).slice(8, -1)
            }
        },
        3142: function(e) {
            var t = e.exports = {
                version: "2.6.12"
            };
            "number" == typeof __e && (__e = t)
        },
        5526: function(e, t, n) {
            var r = n(3749);
            e.exports = function(e, t, n) {
                if (r(e),
                void 0 === t)
                    return e;
                switch (n) {
                case 1:
                    return function(n) {
                        return e.call(t, n)
                    }
                    ;
                case 2:
                    return function(n, r) {
                        return e.call(t, n, r)
                    }
                    ;
                case 3:
                    return function(n, r, o) {
                        return e.call(t, n, r, o)
                    }
                }
                return function() {
                    return e.apply(t, arguments)
                }
            }
        },
        2306: function(e) {
            e.exports = function(e) {
                if (null == e)
                    throw TypeError("Can't call method on  " + e);
                return e
            }
        },
        7498: function(e, t, n) {
            e.exports = !n(9880)((function() {
                return 7 != Object.defineProperty({}, "a", {
                    get: function() {
                        return 7
                    }
                }).a
            }
            ))
        },
        2004: function(e, t, n) {
            var r = n(2799)
              , o = n(5505).document
              , i = r(o) && r(o.createElement);
            e.exports = function(e) {
                return i ? o.createElement(e) : {}
            }
        },
        8760: function(e) {
            e.exports = "constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf".split(",")
        },
        2069: function(e, t, n) {
            var r = n(5505)
              , o = n(3142)
              , i = n(5526)
              , a = n(5954)
              , c = n(9761)
              , u = function(e, t, n) {
                var s, f, d, l = e & u.F, p = e & u.G, g = e & u.S, v = e & u.P, m = e & u.B, h = e & u.W, y = p ? o : o[t] || (o[t] = {}), w = y.prototype, b = p ? r : g ? r[t] : (r[t] || {}).prototype;
                for (s in p && (n = t),
                n)
                    (f = !l && b && void 0 !== b[s]) && c(y, s) || (d = f ? b[s] : n[s],
                    y[s] = p && "function" != typeof b[s] ? n[s] : m && f ? i(d, r) : h && b[s] == d ? function(e) {
                        var t = function(t, n, r) {
                            if (this instanceof e) {
                                switch (arguments.length) {
                                case 0:
                                    return new e;
                                case 1:
                                    return new e(t);
                                case 2:
                                    return new e(t,n)
                                }
                                return new e(t,n,r)
                            }
                            return e.apply(this, arguments)
                        };
                        return t.prototype = e.prototype,
                        t
                    }(d) : v && "function" == typeof d ? i(Function.call, d) : d,
                    v && ((y.virtual || (y.virtual = {}))[s] = d,
                    e & u.R && w && !w[s] && a(w, s, d)))
            };
            u.F = 1,
            u.G = 2,
            u.S = 4,
            u.P = 8,
            u.B = 16,
            u.W = 32,
            u.U = 64,
            u.R = 128,
            e.exports = u
        },
        9880: function(e) {
            e.exports = function(e) {
                try {
                    return !!e()
                } catch (e) {
                    return !0
                }
            }
        },
        5505: function(e) {
            var t = e.exports = "undefined" != typeof window && window.Math == Math ? window : "undefined" != typeof self && self.Math == Math ? self : Function("return this")();
            "number" == typeof __g && (__g = t)
        },
        9761: function(e) {
            var t = {}.hasOwnProperty;
            e.exports = function(e, n) {
                return t.call(e, n)
            }
        },
        5954: function(e, t, n) {
            var r = n(5584)
              , o = n(5734);
            e.exports = n(7498) ? function(e, t, n) {
                return r.f(e, t, o(1, n))
            }
            : function(e, t, n) {
                return e[t] = n,
                e
            }
        },
        4053: function(e, t, n) {
            e.exports = !n(7498) && !n(9880)((function() {
                return 7 != Object.defineProperty(n(2004)("div"), "a", {
                    get: function() {
                        return 7
                    }
                }).a
            }
            ))
        },
        399: function(e, t, n) {
            var r = n(9606);
            e.exports = Object("z").propertyIsEnumerable(0) ? Object : function(e) {
                return "String" == r(e) ? e.split("") : Object(e)
            }
        },
        2799: function(e) {
            e.exports = function(e) {
                return "object" == typeof e ? null !== e : "function" == typeof e
            }
        },
        6124: function(e) {
            e.exports = !0
        },
        3857: function(e, t, n) {
            var r = n(2445)("meta")
              , o = n(2799)
              , i = n(9761)
              , a = n(5584).f
              , c = 0
              , u = Object.isExtensible || function() {
                return !0
            }
              , s = !n(9880)((function() {
                return u(Object.preventExtensions({}))
            }
            ))
              , f = function(e) {
                a(e, r, {
                    value: {
                        i: "O" + ++c,
                        w: {}
                    }
                })
            }
              , d = e.exports = {
                KEY: r,
                NEED: !1,
                fastKey: function(e, t) {
                    if (!o(e))
                        return "symbol" == typeof e ? e : ("string" == typeof e ? "S" : "P") + e;
                    if (!i(e, r)) {
                        if (!u(e))
                            return "F";
                        if (!t)
                            return "E";
                        f(e)
                    }
                    return e[r].i
                },
                getWeak: function(e, t) {
                    if (!i(e, r)) {
                        if (!u(e))
                            return !0;
                        if (!t)
                            return !1;
                        f(e)
                    }
                    return e[r].w
                },
                onFreeze: function(e) {
                    return s && d.NEED && u(e) && !i(e, r) && f(e),
                    e
                }
            }
        },
        3826: function(e, t, n) {
            "use strict";
            var r = n(7498)
              , o = n(9665)
              , i = n(5261)
              , a = n(8598)
              , c = n(7765)
              , u = n(399)
              , s = Object.assign;
            e.exports = !s || n(9880)((function() {
                var e = {}
                  , t = {}
                  , n = Symbol()
                  , r = "abcdefghijklmnopqrst";
                return e[n] = 7,
                r.split("").forEach((function(e) {
                    t[e] = e
                }
                )),
                7 != s({}, e)[n] || Object.keys(s({}, t)).join("") != r
            }
            )) ? function(e, t) {
                for (var n = c(e), s = arguments.length, f = 1, d = i.f, l = a.f; s > f; )
                    for (var p, g = u(arguments[f++]), v = d ? o(g).concat(d(g)) : o(g), m = v.length, h = 0; m > h; )
                        p = v[h++],
                        r && !l.call(g, p) || (n[p] = g[p]);
                return n
            }
            : s
        },
        5584: function(e, t, n) {
            var r = n(8891)
              , o = n(4053)
              , i = n(923)
              , a = Object.defineProperty;
            t.f = n(7498) ? Object.defineProperty : function(e, t, n) {
                if (r(e),
                t = i(t, !0),
                r(n),
                o)
                    try {
                        return a(e, t, n)
                    } catch (e) {}
                if ("get"in n || "set"in n)
                    throw TypeError("Accessors not supported!");
                return "value"in n && (e[t] = n.value),
                e
            }
        },
        5261: function(e, t) {
            t.f = Object.getOwnPropertySymbols
        },
        5064: function(e, t, n) {
            var r = n(9761)
              , o = n(4188)
              , i = n(4351)(!1)
              , a = n(1273)("IE_PROTO");
            e.exports = function(e, t) {
                var n, c = o(e), u = 0, s = [];
                for (n in c)
                    n != a && r(c, n) && s.push(n);
                for (; t.length > u; )
                    r(c, n = t[u++]) && (~i(s, n) || s.push(n));
                return s
            }
        },
        9665: function(e, t, n) {
            var r = n(5064)
              , o = n(8760);
            e.exports = Object.keys || function(e) {
                return r(e, o)
            }
        },
        8598: function(e, t) {
            t.f = {}.propertyIsEnumerable
        },
        2113: function(e, t, n) {
            var r = n(2069)
              , o = n(3142)
              , i = n(9880);
            e.exports = function(e, t) {
                var n = (o.Object || {})[e] || Object[e]
                  , a = {};
                a[e] = t(n),
                r(r.S + r.F * i((function() {
                    n(1)
                }
                )), "Object", a)
            }
        },
        5734: function(e) {
            e.exports = function(e, t) {
                return {
                    enumerable: !(1 & e),
                    configurable: !(2 & e),
                    writable: !(4 & e),
                    value: t
                }
            }
        },
        1273: function(e, t, n) {
            var r = n(8427)("keys")
              , o = n(2445);
            e.exports = function(e) {
                return r[e] || (r[e] = o(e))
            }
        },
        8427: function(e, t, n) {
            var r = n(3142)
              , o = n(5505)
              , i = "__core-js_shared__"
              , a = o[i] || (o[i] = {});
            (e.exports = function(e, t) {
                return a[e] || (a[e] = void 0 !== t ? t : {})
            }
            )("versions", []).push({
                version: r.version,
                mode: n(6124) ? "pure" : "global",
                copyright: "\xa9 2020 Denis Pushkarev (zloirock.ru)"
            })
        },
        2360: function(e, t, n) {
            var r = n(4817)
              , o = Math.max
              , i = Math.min;
            e.exports = function(e, t) {
                return (e = r(e)) < 0 ? o(e + t, 0) : i(e, t)
            }
        },
        4817: function(e) {
            var t = Math.ceil
              , n = Math.floor;
            e.exports = function(e) {
                return isNaN(e = +e) ? 0 : (e > 0 ? n : t)(e)
            }
        },
        4188: function(e, t, n) {
            var r = n(399)
              , o = n(2306);
            e.exports = function(e) {
                return r(o(e))
            }
        },
        2642: function(e, t, n) {
            var r = n(4817)
              , o = Math.min;
            e.exports = function(e) {
                return e > 0 ? o(r(e), 9007199254740991) : 0
            }
        },
        7765: function(e, t, n) {
            var r = n(2306);
            e.exports = function(e) {
                return Object(r(e))
            }
        },
        923: function(e, t, n) {
            var r = n(2799);
            e.exports = function(e, t) {
                if (!r(e))
                    return e;
                var n, o;
                if (t && "function" == typeof (n = e.toString) && !r(o = n.call(e)))
                    return o;
                if ("function" == typeof (n = e.valueOf) && !r(o = n.call(e)))
                    return o;
                if (!t && "function" == typeof (n = e.toString) && !r(o = n.call(e)))
                    return o;
                throw TypeError("Can't convert object to primitive value")
            }
        },
        2445: function(e) {
            var t = 0
              , n = Math.random();
            e.exports = function(e) {
                return "Symbol(".concat(void 0 === e ? "" : e, ")_", (++t + n).toString(36))
            }
        },
        2966: function(e, t, n) {
            var r = n(2069);
            r(r.S, "Date", {
                now: function() {
                    return (new Date).getTime()
                }
            })
        },
        6285: function(e, t, n) {
            var r = n(2069);
            r(r.S + r.F, "Object", {
                assign: n(3826)
            })
        },
        3706: function(e, t, n) {
            var r = n(2069);
            r(r.S + r.F * !n(7498), "Object", {
                defineProperty: n(5584).f
            })
        },
        3176: function(e, t, n) {
            var r = n(2799)
              , o = n(3857).onFreeze;
            n(2113)("freeze", (function(e) {
                return function(t) {
                    return e && r(t) ? e(o(t)) : t
                }
            }
            ))
        },
        7462: function(e, t, n) {
            var r = n(7765)
              , o = n(9665);
            n(2113)("keys", (function() {
                return function(e) {
                    return o(r(e))
                }
            }
            ))
        },
        5764: function(e, t, n) {
            e.exports = n(17)
        },
        6547: function(e, t, n) {
            e.exports = n(7606)
        },
        6770: function(e, t, n) {
            e.exports = n(1225)
        },
        9274: function(e, t, n) {
            e.exports = n(5339)
        },
        5245: function(e, t, n) {
            e.exports = n(2034)
        },
        7785: function(e, t, n) {
            e.exports = n(4799)
        }
    }
      , t = {};
    function n(r) {
        var o = t[r];
        if (void 0 !== o)
            return o.exports;
        var i = t[r] = {
            exports: {}
        };
        return e[r](i, i.exports, n),
        i.exports
    }
    n.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return n.d(t, {
            a: t
        }),
        t
    }
    ,
    n.d = function(e, t) {
        for (var r in t)
            n.o(t, r) && !n.o(e, r) && Object.defineProperty(e, r, {
                enumerable: !0,
                get: t[r]
            })
    }
    ,
    n.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    n.p = "//g.alicdn.com/zgc/aem-assets-logger/0.0.13/",
    n.p = window.__ASSET_PATH__,
    function() {
        "use strict";
        var e = n(6547)
          , t = n.n(e)
          , r = "undefined" != typeof my && !!my && "function" == typeof my.showToast
          , o = "undefined" != typeof wx && !!wx && (void 0 !== wx.login || void 0 !== wx.miniProgram);
        function i(e, t) {
            "function" == typeof requestIdleCallback ? requestIdleCallback(e, {
                timeout: t || 1e3
            }) : setTimeout(e, 0)
        }
        function a(e) {
            return "undefined" != typeof Promise && e instanceof Promise
        }
        var c = {}
          , u = "maxUrlLength"
          , s = function() {
            if (!r || !o)
                return !1;
            try {
                var e = "";
                try {
                    e = navigator ? navigator.userAgent || navigator.swuserAgent : ""
                } catch (e) {}
                if (!e)
                    try {
                        e = clientInformation ? clientInformation.appVersion : ""
                    } catch (e) {}
                var t = !1;
                try {
                    t = !!dd
                } catch (e) {}
                return t || /AliApp\(AP/.test(e) || /AliApp\(DingTalk/.test(e) || /micromessenger/.test(e)
            } catch (e) {
                return !1
            }
        }() ? 5e3 : 35e3
          , f = []
          , d = []
          , l = "requiredFields"
          , p = function e() {
            var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 20
              , n = arguments.length > 1 ? arguments[1] : void 0;
            return n = n || "",
            t ? e(--t, "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz".charAt(Math.floor(60 * Math.random())) + n) : n
        }
          , g = {
            sdk_version: "1.0.34",
            pv_id: p()
        };
        function v() {
            if (f.length) {
                var e = f.join("|");
                if (s = g.maxUrlLength || s,
                e.length < s)
                    return f = [],
                    void c.send(h(e));
                for (var t = ""; f.length; ) {
                    var n = f[0];
                    if (t && (t + "|" + n).length > s)
                        break;
                    f.shift(),
                    t += t ? "|" + n : n
                }
                c.send(h(t)),
                f.length && v()
            }
        }
        function m(e, t) {
            !1 === t ? i((function() {
                c.send(h(e))
            }
            )) : (f.push(e),
            i(v))
        }
        function h(e) {
            var t = ["msg=" + e];
            for (var n in g)
                -1 === n.indexOf("plugin_") && n !== l && n !== u && g.hasOwnProperty(n) && (g[n] || 0 === g[n]) && t.push(n + "=" + encodeURIComponent(g[n]));
            return t.join("&")
        }
        function y() {
            return (g.requiredFields || []).concat(["pid"]).some((function(e) {
                return void 0 === g[e]
            }
            ))
        }
        c.setConfig = function(e, t) {
            var n = function() {
                if (void 0 !== t)
                    g[e] = t;
                else
                    for (var n in e)
                        g[n] = e[n]
            };
            d.length ? (n(),
            y() || (d.forEach((function(e) {
                m.apply(null, e)
            }
            )),
            d = [])) : (function() {
                if (void 0 !== t)
                    return t !== g[e];
                for (var n in e)
                    if (e[n] !== g[n])
                        return !0;
                return !1
            }() && v(),
            n())
        }
        ,
        c.getConfig = function(e) {
            return e ? g[e] : g
        }
        ,
        c.updatePVID = function() {
            c.setConfig("pv_id", p())
        }
        ,
        c.log = function(e) {
            var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
              , r = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {};
            if (e) {
                n.ts = n.ts || (new Date).getTime(),
                n.type = e;
                var o = [];
                for (var i in n) {
                    var a = n[i]
                      , c = Object.prototype.toString.call(a);
                    "[object String]" !== c && "[object Number]" !== c && "[object Boolean]" !== c && "[object Object]" !== c && "[object Array]" !== c || ("[object Object]" !== c && "[object Array]" !== c || (a = t()(a)),
                    o.push("".concat(i, "=").concat(encodeURIComponent(a))))
                }
                n = encodeURIComponent(o.join("&")),
                y() ? d.push([n, r.combo]) : m(n, r.combo)
            }
        }
        ,
        c.before = function(e, t) {
            return function() {
                var n = arguments
                  , r = t.apply(c, n);
                a(r) ? r.then((function(t) {
                    e.apply(c, t || n)
                }
                )) : e.apply(c, r || n)
            }
        }
        ,
        c.after = function(e, t) {
            return function() {
                var n = arguments;
                e.apply(c, n),
                t.apply(c, n)
            }
        }
        ;
        var w = c;
        var b = -1 !== navigator.userAgent.indexOf("WindVane")
          , _ = [];
        w.setConfig(function() {
            var e = function() {
                if (window.goldlog && goldlog.spm_ab)
                    return goldlog.spm_ab;
                var e, t = document.querySelector('meta[name="spm-id"]') || document.querySelector('meta[name="data-spm"]');
                if (t && (e = t.content) && -1 !== e.indexOf("."))
                    return e.split(".");
                var n = document.body && document.body.getAttribute("data-spm");
                return e && n ? [e, n] : []
            }()
              , t = {
                title: document.title,
                spm_a: e[0],
                spm_b: e[1],
                hash: location.hash,
                dpi: window.devicePixelRatio,
                sr: "".concat(window.screen.width, "x").concat(window.screen.height)
            }
              , n = document.querySelector('meta[name="aes-config"]');
            if (n)
                try {
                    var r = n.getAttribute("content");
                    r && r.split("&").forEach((function(e) {
                        var n = e.split("=")
                          , r = n[0]
                          , o = decodeURIComponent(n[1]);
                        if (-1 !== r.indexOf(".")) {
                            var i = r.split(".")[0]
                              , a = r.split(".")[1];
                            t[i] || (t[i] = {}),
                            t[i][a] = o
                        } else
                            t[r] = o
                    }
                    ))
                } catch (e) {}
            for (var o in window.AES_CONFIG)
                t[o] = AES_CONFIG[o];
            return t
        }()),
        window.addEventListener("hashchange", (function() {
            w.setConfig("hash", location.hash)
        }
        ));
        var O = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
        if (O) {
            var T = function() {
                w.setConfig({
                    downlink: O.downlink,
                    net_type: O.effectiveType
                }),
                navigator.onLine && _.length && (_.forEach((function(e) {
                    i((function() {
                        w.send(e)
                    }
                    ))
                }
                )),
                _ = [])
            };
            T(),
            O.addEventListener("change", T)
        }
        try {
            var x = function() {
                var e = document.querySelector("title");
                e && new MutationObserver((function() {
                    w.setConfig("title", document.title)
                }
                )).observe(e, {
                    childList: !0,
                    characterData: !0,
                    subtree: !0
                })
            };
            document.querySelector("title") ? x() : document.addEventListener("DOMContentLoaded", x)
        } catch (e) {}
        w.log = w.before(w.log, (function() {
            var e;
            if (window.goldlog) {
                var t = goldlog.spm_ab;
                t && (w.getConfig("spm_a") !== t[0] && ((e || (e = {})).spm_a = t[0]),
                w.getConfig("spm_b") !== t[1] && ((e || (e = {})).spm_b = t[1]))
            }
            var n = function() {
                try {
                    if (window.xr) {
                        var e = Array.from(xr.global.recordingContexts.keys());
                        if (e.length > 0) {
                            var t = xr.global.recordingContexts.get(e[0]);
                            if (t.appKey && t.recordingId && t.isRecording)
                                return {
                                    appKey: t.appKey,
                                    recordingId: t.recordingId
                                }
                        }
                    }
                } catch (e) {}
            }();
            if (n) {
                var r = n.appKey + "," + n.recordingId;
                w.getConfig("xreplay_id") !== r && ((e || (e = {})).xreplay_id = r)
            }
            e && w.setConfig(e)
        }
        )),
        w.send = function(e) {
            var t = window.goldlog && "function" == typeof goldlog.record;
            if (navigator.onLine || b && t) {
                var n, r = ["/aes.1.1", "EXP", e, window.AES_DISABLE_POST ? "GET" : "POST"];
                if (t)
                    (n = goldlog).record.apply(n, r);
                else
                    window.goldlog_queue || (window.goldlog_queue = []),
                    goldlog_queue.push({
                        action: "goldlog.record",
                        arguments: r
                    })
            } else
                _.length > 500 && _.shift(),
                _.push(e)
        }
        ;
        ["AES_QUEUE", "AES_QUENE"].forEach((function(e) {
            "[object Array]" === Object.prototype.toString.call(window[e]) ? window[e].forEach((function(e) {
                "function" == typeof e ? e(w) : w[e.action].apply(w, e.arguments)
            }
            )) : window[e] = [],
            window[e].push = function(e) {
                "function" == typeof e ? e(w) : w[e.action].apply(w, e.arguments)
            }
        }
        ));
        var E = w
          , A = {
            noop: function() {},
            win: "object" == typeof window && window.document ? window : void 0,
            T: function(e, t) {
                var n = Object.prototype.toString.call(e).substring(8).replace("]", "");
                return t ? n === t : n
            },
            on: function(e, t, n, r, o) {
                return e.addEventListener ? (o = o || !1,
                e.addEventListener(t, (function i(a) {
                    r && e.removeEventListener(t, i, o),
                    n.call(this, a)
                }
                ), o)) : e.attachEvent && e.attachEvent("on" + t, (function o(i) {
                    r && e.detachEvent("on" + t, o),
                    n.call(this, i)
                }
                )),
                this
            },
            off: function(e, t, n) {
                return n ? (e.removeEventListener ? e.removeEventListener(t, n) : e.detachEvent && e.detachEvent(t, n),
                this) : this
            }
        }
          , N = A
          , S = {};
        function L(e) {
            if (void 0 !== typeof e)
                return S[e]
        }
        function k(e) {
            return e ? e.length < 1001 ? e : e.substr(0, 997) + "..." : ""
        }
        function C(e) {
            if (!e || "string" != typeof e)
                return "";
            try {
                var t = e.split("\n").slice(1).map((function(e) {
                    return e.replace(/^\s+at\s+/, "")
                }
                )).filter((function(e) {
                    return !!e
                }
                ));
                if (t.join("^").length <= 2e3)
                    return t.join("^");
                for (var n = !1; t.join("^").length > 2e3; )
                    if (2 === t.length)
                        t.splice(1, 1),
                        n = !0;
                    else if (1 === t.length) {
                        var r = t[0];
                        t[0] = "".concat(r.substr(0, 997), "...").concat(r.substr(-1e3, 1e3))
                    } else
                        t.splice(t.length - 2),
                        n = !0;
                if (t.length > 1 && n) {
                    var o = t.pop();
                    return t.join("^") + "^...^" + o
                }
                return 1 === t.length && n ? t[0] + "^..." : t.join("^")
            } catch (e) {
                return ""
            }
        }
        function j(e) {
            if ("string" == typeof e.message) {
                var t = e.message.match(/Uncaught (\w+):/);
                if (t && t[1])
                    return t[1]
            }
            return e.error_type ? e.error_type : e.name ? e.name : e.constructor.name
        }
        var I = function(e) {
            if ("object" == typeof e) {
                var t = L("AES")
                  , n = e.message
                  , r = void 0 === n ? "" : n
                  , o = e.filename
                  , i = e.lineno
                  , a = e.colno
                  , c = e.stack
                  , u = e.error_code
                  , s = void 0 === u ? "" : u
                  , f = e.error
                  , d = (t.getConfig("plugin_jserror") || {}).ignoreList;
                d && d.some((function(t) {
                    if ("string" == typeof t)
                        return t === r;
                    if ("function" == typeof t)
                        try {
                            return t(r, e)
                        } catch (e) {}
                    else if (t instanceof RegExp)
                        return t.test(r)
                }
                )) || t.log("js_error", {
                    message: r,
                    url: k(o),
                    lineno: i,
                    colno: a,
                    stack: C(f && f.stack || c),
                    error_type: j(e),
                    error_code: s
                })
            }
        };
        function P(e, t, n, r, o) {
            try {
                if ("string" == typeof e)
                    return void I({
                        message: e,
                        filename: t,
                        lineno: n,
                        colno: r,
                        error: o
                    });
                I(e)
            } catch (e) {}
        }
        function R(e) {
            if (e)
                try {
                    var n = ""
                      , r = 0
                      , o = 0
                      , i = ""
                      , a = ""
                      , c = "string" == typeof e ? e : e.reason
                      , u = L("AES").getConfig("plugin_js_error_processPromiseRejectReason");
                    if ("function" == typeof u && (!1 === (c = u(c)) || void 0 === c || "" === c || null === c))
                        return;
                    "string" == typeof e.message && (n = e.message),
                    "string" == typeof c ? n = c : "object" == typeof c && (n = c.message);
                    try {
                        n || (n = "object" == typeof c ? t()(c).substr(0, 150) : n)
                    } catch (e) {}
                    if ("object" == typeof c) {
                        if ("number" == typeof c.column)
                            o = c.column,
                            r = c.line;
                        else if (c.stack) {
                            (s = c.stack.match(/at\s+.+:(\d+):(\d+)/)) && (r = s[1],
                            o = s[2])
                        }
                        if (c.sourceURL)
                            i = c.sourceURL;
                        else if (c.stack) {
                            var s;
                            (s = c.stack.match(/at\s+(.+):\d+:\d+/)) && (i = s[1])
                        }
                        c.stack && (a = c.stack)
                    }
                    I({
                        message: n,
                        filename: i,
                        lineno: r,
                        colno: o,
                        stack: a,
                        error_type: e.constructor.name
                    })
                } catch (e) {}
        }
        var D, U, M = P, F = R;
        U = E,
        void 0 !== typeof (D = "AES") && (S[D] = U);
        var G = M
          , H = F;
        !function() {
            var e = E.getConfig("plugin_jserror") || {};
            window && !window.AESPluginJsError && (N.on(window, "error", G),
            !e.disable_unhandled_rejection && N.on(window, "unhandledrejection", H))
        }();
        function q(e, t) {
            for (var n in t)
                e[n] = t[n];
            return e
        }
        function B(e) {
            var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 1e3;
            if ("string" == typeof e)
                return e.length > t && (e = e.substr(0, t - 3) + "..."),
                e
        }
        var Y = function(e) {
            var t = e.url
              , n = e.success
              , r = e.msg
              , o = e.status
              , i = e.code
              , a = e.duration
              , c = e.traceId
              , u = e.params
              , s = e.body
              , f = e.response
              , d = e.headers
              , l = e.rtype
              , p = e.method
              , g = E.getConfig("plugin_api") || {}
              , v = g.ignoreList
              , m = g.sendResponseOnSuccess;
            if (!v || !v.some((function(n) {
                if ("string" == typeof n)
                    return n === t;
                if ("function" == typeof n)
                    try {
                        return n(t, e)
                    } catch (e) {}
                else if (n instanceof RegExp)
                    return n.test(t)
            }
            ))) {
                var h = function() {
                    if ("object" != typeof my)
                        return !1;
                    try {
                        var e = "";
                        try {
                            e = navigator ? navigator.userAgent || navigator.swuserAgent : ""
                        } catch (e) {}
                        if (!e)
                            try {
                                e = clientInformation ? clientInformation.appVersion : ""
                            } catch (e) {}
                        var t = !1;
                        try {
                            t = !!dd
                        } catch (e) {}
                        return t || /AliApp\(AP/.test(e) || /AliApp\(DingTalk/.test(e) || /micromessenger/.test(e)
                    } catch (e) {
                        return !1
                    }
                }();
                E.log("api", {
                    url: t,
                    method: "string" == typeof p ? p.toUpperCase() : void 0,
                    success: n,
                    msg: r,
                    status: o,
                    code: i,
                    duration: a,
                    trace_id: c,
                    params: u,
                    body: B(s, h ? 2e3 : 1e4),
                    response: !n || m ? B(f, h ? 1e3 : 1e4) : void 0,
                    headers: d,
                    rtype: l
                })
            }
        };
        function K(e, t) {
            return (void 0 === t || t >= 200 && t < 300) && (void 0 !== e.success ? !0 === e.success || "true" === e.success : void 0 !== e.isSuccess ? !0 === e.isSuccess || "true" === e.isSuccess : void 0 !== e.isOk ? !0 === e.isOk || "true" === e.isOk : void 0 !== e.ok ? !0 === e.ok || "true" === e.ok : isNaN(e.status) ? !!isNaN(e.code) || 200 == e.code : 200 == e.status)
        }
        function z(e) {
            return e.code
        }
        function W(e) {
            var t = e.msg || e.message || e.errMsg || e.errorMessage || e.errorMsg;
            return t && t.length > 50 && (t = t.substring(1, 50)),
            t
        }
        function J(e, t) {
            if (t = t.toUpperCase(),
            e && ("POST" === t || "PUT" === t)) {
                if ("string" == typeof e)
                    return e;
                if (window.FormData && e instanceof FormData) {
                    var n = [];
                    return e.forEach((function(e, t) {
                        n.push("".concat(t, "=").concat("string" == typeof e ? e : Object.prototype.toString.call(e)))
                    }
                    )),
                    n.join("&")
                }
                return window.URLSearchParams && e instanceof URLSearchParams ? e.toString() : window.Request && e instanceof Request ? e.clone().text() : Object.prototype.toString.call(e)
            }
        }
        function X(e, t, n) {
            var r, o = e;
            if ("string" == typeof o)
                try {
                    o = JSON.parse(e)
                } catch (e) {}
            r = "[object Object]" === Object.prototype.toString.call(o) ? {
                msg: W(o),
                code: z(o),
                success: K(o, t)
            } : {
                success: void 0 === t || t >= 200 && t < 300
            };
            var i = E.getConfig("plugin_api") || {};
            if ("function" == typeof i.parseResponse)
                try {
                    var a = i.parseResponse(o, t, n) || {};
                    for (var c in a)
                        r[c] = a[c]
                } catch (e) {}
            return r
        }
        function V(e) {
            return !e || -1 !== e.indexOf("api=") && -1 !== e.indexOf("v=") && -1 !== e.indexOf("jsv=") || -1 !== e.indexOf(".mmstat.com") || e.match(/\.(js|css|png|jpg|gif|jpeg|webp|ico|svg)(\?.*)?$/)
        }
        function $(e) {
            return "undefined" != typeof Promise && e instanceof Promise
        }
        function Q(e) {
            if (window.Headers && e instanceof Headers) {
                var t = {};
                return e.forEach((function(e, n) {
                    t[n] = e
                }
                )),
                t
            }
            if ("[object Object]" === Object.prototype.toString.call(e))
                return e
        }
        function Z(e, t) {
            if (t.originResponse)
                return e;
            if ("jsonp" === t.method)
                return e.text();
            var n = e.headers && e.headers.get ? e.headers.get("content-type") : null;
            return n && -1 === n.toLowerCase().indexOf("json") && -1 === n.toLowerCase().indexOf("text") ? "[".concat(n, "]") : e.text()
        }
        var ee = function() {
            if (!("function" != typeof window.fetch || window.fetch && window.fetch.polyfill)) {
                var e = window.fetch;
                window.fetch = function(t) {
                    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
                      , r = E.getConfig("plugin_api") || {};
                    if ("HEAD" === n.method || "no-cors" === n.mode)
                        return e.apply(window, arguments);
                    var o = "object" == typeof t ? t.url || t.href : t;
                    if (V(o))
                        return e.apply(window, arguments);
                    var i, a, c = o.split("?"), u = c[0], s = c[1], f = n.method || t.method || "GET";
                    try {
                        a = Q(n.headers || t.headers)
                    } catch (e) {}
                    try {
                        $(i = J(n.body || t, f)) && i.then((function(e) {
                            i = e
                        }
                        ))
                    } catch (e) {}
                    var d = (new Date).getTime();
                    return e.apply(window, arguments).then((function(e) {
                        try {
                            if ("[object Response]" !== Object.prototype.toString.call(e))
                                return e;
                            var t, o = (new Date).getTime() - d, c = e.clone ? e.clone() : e, l = c.status;
                            c.headers.has("eagleeye-traceid") ? t = c.headers.get("eagleeye-traceid") : c.headers.has("x-eagleeye-id") && (t = c.headers.get("x-eagleeye-id"));
                            var p = function(e) {
                                !1 !== (c = X(e, l, {
                                    type: "fetch",
                                    params: s,
                                    url: u,
                                    body: n.body
                                })).success && r.disable_send_on_success || Y(q({
                                    url: u,
                                    method: f,
                                    status: l,
                                    duration: o,
                                    traceId: t,
                                    params: s,
                                    headers: a,
                                    body: i,
                                    response: e,
                                    rtype: "fetch"
                                }, c))
                            }
                              , g = Z(c, n);
                            $(g) ? g.then(p) : p(g)
                        } catch (e) {}
                        return e
                    }
                    ), (function(e) {
                        var t = (new Date).getTime() - d
                          , n = X("", -1, {
                            type: "fetch",
                            params: s,
                            url: u
                        });
                        throw Y(q({
                            url: u,
                            method: f,
                            success: !1,
                            msg: e.message,
                            status: -1,
                            duration: t,
                            params: s,
                            body: i,
                            headers: a,
                            rtype: "fetch"
                        }, n)),
                        e
                    }
                    ))
                }
            }
        };
        var te = function() {
            if ("function" == typeof window.XMLHttpRequest && window.addEventListener) {
                var e = window.XMLHttpRequest
                  , t = e.prototype
                  , n = t.open
                  , r = t.send
                  , o = t.setRequestHeader;
                e.prototype.open = function(e, t) {
                    n.apply(this, arguments),
                    this._aesHook = {
                        method: e,
                        url: t
                    }
                }
                ,
                e.prototype.setRequestHeader = function(e, t) {
                    o.apply(this, arguments),
                    this._aesHook.headers || (this._aesHook.headers = {}),
                    this._aesHook.headers[e] = t
                }
                ,
                e.prototype.send = function(e) {
                    r.apply(this, arguments);
                    try {
                        var t = this._aesHook
                          , n = t.url
                          , o = t.method
                          , i = void 0 === o ? "GET" : o
                          , a = t.headers;
                        delete this._aesHook;
                        var c = n ? n.href || n : "";
                        if (V(c))
                            return;
                        var u, s = c.split("?"), f = this, d = 0, l = s[1], p = (new Date).getTime();
                        n = s[0];
                        try {
                            u = J(e, i)
                        } catch (e) {}
                        var g = function() {
                            d = f.status || d;
                            var t, r = (new Date).getTime() - p;
                            try {
                                var o = f.getAllResponseHeaders();
                                -1 !== o.indexOf("eagleeye-traceid") ? t = f.getResponseHeader("eagleeye-traceid") : -1 !== o.indexOf("x-eagleeye-id") && (t = f.getResponseHeader("x-eagleeye-id"))
                            } catch (e) {}
                            var c, s = f.responseType || "text";
                            "text" === s || "json" === s ? c = f.response : f.response && (c = Object.prototype.toString.call(f.response));
                            var g = X(c || "", d, {
                                type: "xhr",
                                params: l,
                                url: n,
                                body: e
                            })
                              , v = E.getConfig("plugin_api") || {};
                            g.success && v.disable_send_on_success || Y(q({
                                url: n,
                                method: i,
                                status: d,
                                duration: r,
                                traceId: t,
                                params: l,
                                headers: a,
                                body: u,
                                response: c,
                                rtype: "xhr"
                            }, g))
                        };
                        void 0 !== f.onloadend ? (f.addEventListener("abort", (function() {
                            d = -2
                        }
                        )),
                        f.addEventListener("timeout", (function() {
                            d = -3
                        }
                        )),
                        f.addEventListener("loadend", g)) : f.addEventListener("readystatechange", (function() {
                            4 === f.readyState && g()
                        }
                        ))
                    } catch (e) {}
                }
            }
        }
          , ne = n(9274)
          , re = n.n(ne);
        var oe = function() {
            function e(e) {
                var n = this.options
                  , r = this.params
                  , o = (new Date).getTime();
                return e().then((function() {
                    var e = n.retJson.ret
                      , i = (new Date).getTime() - o;
                    e instanceof Array && (e = e.join(","));
                    var a = E.getConfig("plugin_api") || {}
                      , c = {};
                    if ("function" == typeof a.parseResponse)
                        try {
                            c = a.parseResponse(n.retJson, "", {
                                type: "mtop",
                                params: r.data,
                                url: r.api
                            }) || {}
                        } catch (e) {}
                    var u = void 0 === c.success ? -1 === e.indexOf("SUCCESS") : !c.success;
                    if (u || !a.disable_send_on_success) {
                        var s, f, d, l = n.retJson.code || 200, p = n.retJson.responseHeaders;
                        if ("string" == typeof p) {
                            var g = p.match(/(x-eagleeye-id|eagleeye-traceid):\s*([a-z0-9]+)/);
                            g && (s = g[2]);
                            var v = p.match(/status:\s*(\d+)/);
                            v && (l = v[1])
                        }
                        if (e) {
                            var m = e.split("::");
                            f = m[0],
                            d = m[1]
                        }
                        Y(q({
                            url: r.api,
                            success: !u,
                            method: r.type || "GET",
                            msg: d,
                            status: l,
                            code: f,
                            duration: i,
                            traceId: s,
                            params: r.data,
                            response: t()(n.retJson),
                            rtype: "mtop"
                        }, c))
                    }
                }
                ))
            }
            var n;
            window.lib || (window.lib = {}),
            lib.mtop ? lib.mtop.middlewares && lib.mtop.middlewares.push(e) : re()(lib, "mtop", {
                configurable: !0,
                set: function(t) {
                    var r;
                    (n = t).middlewares ? -1 === n.middlewares.indexOf(e) && n.middlewares.push(e) : re()(n, "middlewares", {
                        configurable: !0,
                        set: function(t) {
                            -1 === (r = t).indexOf(e) && r.push(e)
                        },
                        get: function() {
                            return r
                        }
                    })
                },
                get: function() {
                    return n
                }
            })
        }
          , ie = {
            hookFetch: ee,
            hookXHR: te,
            hookMtop: oe
        };
        !function() {
            if (!window.__AES_PLUGIN_API__) {
                window.__AES_PLUGIN_API__ = !0;
                var e = E.getConfig("plugin_api") || {}
                  , t = e.disableHook
                  , n = e.disableHookFetch
                  , r = e.disableHookXHR
                  , o = e.disableHookMtop;
                if (!0 !== t) {
                    var i = ie.hookXHR
                      , a = ie.hookMtop;
                    !0 !== n && (0,
                    ie.hookFetch)(),
                    !0 !== r && i(),
                    !0 !== o && a()
                }
            }
        }();
        var ae = n(6770)
          , ce = {}
          , ue = null
          , se = 0
          , fe = function() {
            ue && ve(ue),
            (se || ue) && E.log("paint", ce)
        }
          , de = function(e) {
            var t = e.entryType
              , n = e.name
              , r = e.startTime
              , o = e.duration
              , i = e.c1
              , a = e.c2
              , c = e.c3
              , u = e.c4
              , s = e.c5
              , f = e.c6;
            E.log("usertiming", {
                p1: r,
                p2: o,
                p3: t,
                p4: n,
                c1: i,
                c2: a,
                c3: c,
                c4: u,
                c5: s,
                c6: f
            })
        }
          , le = function(e) {
            var t = function(e) {
                return "string" == typeof e || "number" == typeof e ? e : "object" == typeof e && e instanceof HTMLElement ? e.tagName : void 0
            }
              , n = {
                startTime: "p1",
                identifier: "p2",
                name: "p3",
                url: "p4",
                element: "p5",
                naturalHeight: "p6",
                naturalWidth: "p7"
            }
              , r = {};
            for (var o in n)
                void 0 !== e[o] && (r[n[o]] = t(e[o]));
            E.log("elementtiming", r)
        }
          , pe = function() {
            var e, n, r, o, i = E.getConfig("plugin_perf_resourceTimingSampling") || .01;
            if (!(Math.random() >= i) && "function" == typeof window.fetch && null !== (e = window) && void 0 !== e && null !== (n = e.performance) && void 0 !== n && n.getEntries && null !== (r = window) && void 0 !== r && null !== (o = r.performance) && void 0 !== o && o.getEntriesByType) {
                var a = E.getConfig("plugin_perf_resourceTimingThreshhold") || 8e3
                  , c = performance.getEntriesByType("navigation")[0] || window.performance.timing;
                if (c)
                    if (c.loadEventStart - c.fetchStart < a)
                        return;
                var u = performance.getEntries();
                if (u && 0 !== u.length)
                    try {
                        var s = E.getConfig("pv_id")
                          , f = E.getConfig("pid")
                          , d = {
                            __topic__: "resourcetiming",
                            __logs__: [{
                                pid: f,
                                name: s,
                                resource: encodeURIComponent(t()(u.slice(0, 200)))
                            }]
                        };
                        if (!f || !s)
                            return;
                        fetch("https://aes.cn-wulanchabu.log.aliyuncs.com/logstores/aes-resourcetiming/track", {
                            method: "POST",
                            body: t()(d),
                            headers: {
                                "Content-Type": "application/json",
                                "x-log-apiversion": "0.6.0",
                                "x-log-bodyrawsize": "1234"
                            }
                        })
                    } catch (e) {}
            }
        }
          , ge = function(e) {
            ue = e
        }
          , ve = function(e) {
            var t = function(e) {
                return "string" == typeof e || "number" == typeof e ? e : "object" == typeof e && e instanceof HTMLElement ? e.tagName : void 0
            }
              , n = {
                startTime: "p3",
                element: "p4",
                url: "p5"
            };
            for (var r in n)
                void 0 !== e[r] && (ce[n[r]] = t(e[r]))
        }
          , me = (new Date).getTime()
          , he = []
          , ye = function() {
            var e, t, n, r;
            return null !== (e = window) && void 0 !== e && null !== (t = e.performance) && void 0 !== t && t.now ? performance.now() : null !== (n = window) && void 0 !== n && null !== (r = n.performance) && void 0 !== r && r.timing ? (new Date).getTime() - performance.timing.navigationStart : (new Date).getTime() - me
        };
        function we(e, t) {
            for (var n = 0; n < t.length; n++) {
                var r = t[n];
                r.enumerable = r.enumerable || !1,
                r.configurable = !0,
                "value"in r && (r.writable = !0),
                ne(e, r.key, r)
            }
        }
        function be(e, t, n) {
            return t && we(e.prototype, t),
            n && we(e, n),
            ne(e, "prototype", {
                writable: !1
            }),
            e
        }
        var _e;
        _e = function() {
            var e = function() {
                var e, t, n;
                if ((null === (e = window) || void 0 === e || null === (t = e.performance) || void 0 === t || null === (n = t.timing) || void 0 === n ? void 0 : n.navigationStart) > 0) {
                    var r = {};
                    for (var o in performance.timing)
                        "number" == typeof performance.timing[o] && performance.timing[o] > 0 && (r[o] = Math.max(performance.timing[o] - performance.timing.navigationStart, 0));
                    return r
                }
            }();
            e && e.responseStart && e.responseEnd && e.responseEnd >= e.responseStart && E.log("perf", e),
            E.getConfig("plugin_perf_enableResourceTiming") && setTimeout(pe, 5e3)
        }
        ,
        "complete" === document.readyState ? setTimeout(_e) : window.addEventListener("load", (function() {
            return setTimeout(_e)
        }
        ));
        !function() {
            if (window.PerformanceObserver) {
                var e = [];
                E.getConfig("plugin_perf_enableUserTimingObserve") && (window.PerformanceMark && e.push("mark"),
                window.PerformanceMeasure && e.push("measure")),
                window.PerformancePaintTiming && e.push("paint"),
                window.PerformanceElementTiming && e.push("element"),
                window.LargestContentfulPaint && (e.push("largest-contentful-paint"),
                document.addEventListener("visibilitychange", (function e() {
                    document.hidden && (document.removeEventListener("visibilitychange", e, !0),
                    fe())
                }
                ), !0));
                try {
                    !function() {
                        for (var t = {}, n = 0; n < e.length; n++) {
                            var r = e[n]
                              , o = new PerformanceObserver((function(e) {
                                e.getEntries().forEach((function(e) {
                                    switch (e.entryType) {
                                    case "paint":
                                        r = (n = e).name,
                                        o = n.startTime,
                                        (i = {
                                            "first-paint": "p1",
                                            "first-contentful-paint": "p2"
                                        })[r] && (ce[i[r]] = o,
                                        se++,
                                        window.LargestContentfulPaint || 2 !== se || fe());
                                        break;
                                    case "mark":
                                    case "measure":
                                        de(e);
                                        break;
                                    case "element":
                                        t[e.identifier] || (t[e.identifier] = 1,
                                        le(e));
                                        break;
                                    case "largest-contentful-paint":
                                        ge(e)
                                    }
                                    var n, r, o, i
                                }
                                ))
                            }
                            ));
                            try {
                                o.observe({
                                    type: r,
                                    buffered: !0
                                })
                            } catch (t) {
                                o.observe({
                                    entryTypes: e
                                });
                                break
                            }
                        }
                    }()
                } catch (e) {}
            }
        }();
        var Oe, Te = function(e) {
            if (void 0 === e)
                return console.error("Failed to execute 'mark' on 'Performance': 1 argument required, but only 0 present.");
            var t = {
                name: e + "",
                entryType: "mark",
                startTime: ye(),
                duration: 0
            };
            return he.push(t),
            de(t),
            t
        };
        var xe, Ee, Ae = E.getConfig("plugin_pv") || {}, Ne = Ae.autoPV, Se = void 0 === Ne || Ne, Le = Ae.autoLeave, ke = void 0 === Le || Le, Ce = Ae.enableHistory, je = Ae.enableHash, Ie = function(e, t) {
            if (e) {
                var n = t || 500;
                return e.length > n ? e.slice(0, n - 3) + "..." : e
            }
        }, Pe = null === (Oe = document) || void 0 === Oe ? void 0 : Oe.referrer, Re = function() {
            return {
                p1: window.parent !== window,
                p2: Ie(Pe)
            }
        }, De = function() {
            try {
                E.log("leave", Re())
            } catch (e) {}
        }, Ue = !0;
        function Me() {
            Ue ? Ue = !1 : E.updatePVID && E.updatePVID(),
            function() {
                try {
                    E.log("pv", Re())
                } catch (e) {}
            }(),
            Pe = location.href
        }
        (Se && setTimeout((function() {
            Me()
        }
        ), 10),
        Ce && Se ? function(e) {
            var t, n, r, o;
            window.addEventListener("popstate", (function(t) {
                e(t.state)
            }
            ));
            var i = null === (t = window) || void 0 === t || null === (n = t.history) || void 0 === n ? void 0 : n.pushState;
            i && (history.pushState = function(t) {
                i.apply(this, arguments),
                e(t)
            }
            );
            var a = null === (r = window) || void 0 === r || null === (o = r.history) || void 0 === o ? void 0 : o.replaceState;
            a && (history.replaceState = function(t) {
                a.apply(this, arguments),
                e(t)
            }
            )
        }((function() {
            Me()
        }
        )) : je && Se && function(e) {
            window.addEventListener("hashchange", (function() {
                e({
                    page_id: location.hash || "#"
                })
            }
            ))
        }(Me),
        ke) && (xe = function() {
            De()
        }
        ,
        null === (Ee = window) || void 0 === Ee || Ee.addEventListener("beforeunload", xe));
        function Fe() {
            return Fe = ae ? ae.bind() : function(e) {
                for (var t = 1; t < arguments.length; t++) {
                    var n = arguments[t];
                    for (var r in n)
                        Object.prototype.hasOwnProperty.call(n, r) && (e[r] = n[r])
                }
                return e
            }
            ,
            Fe.apply(this, arguments)
        }
        var Ge = n(7785)
          , He = n.n(Ge);
        var qe = n(5764)
          , Be = n.n(qe)
          , Ye = n(2396)
          , Ke = {};
        function ze(e) {
            return e && e instanceof Element ? getComputedStyle(e) : {}
        }
        function We(e) {
            for (var t = function(e) {
                return e ? Number(e.replace("px", "")) : 0
            }, n = function(e, n) {
                n = n || "inner";
                var r = ze(e)
                  , o = t(r.marginLeft)
                  , i = t(r.marginTop)
                  , a = t(r.marginRight)
                  , c = t(r.marginBottom)
                  , u = t(r.borderLeftWidth)
                  , s = t(r.borderTopWidth)
                  , f = t(r.borderRightWidth)
                  , d = t(r.borderBottomWidth)
                  , l = t(r.paddingLeft)
                  , p = t(r.paddingTop)
                  , g = t(r.paddingRight)
                  , v = t(r.paddingBottom)
                  , m = t(r.width)
                  , h = t(r.height);
                return "inner" === n && (m -= l + g + u + f,
                h -= p + v + s + d),
                "outer" === n && (m += o + a,
                h += i + c),
                m * h
            }, r = e, o = 0; r && r !== document.body && r.parentNode && o < 2; ) {
                var i = ze(r)
                  , a = ze(r.parentNode)
                  , c = i.width
                  , u = i.height
                  , s = i.display
                  , f = i.position
                  , d = a.width
                  , l = a.height
                  , p = a.display
                  , g = n(r, "outer")
                  , v = n(r.parentNode, "inner");
                if ("auto" !== d && "auto" !== l || (v = "inline" === p || "inline-block" === p ? g : n(r.parentNode.parentNode || document.body)),
                0 !== v) {
                    if ("auto" === c || "auto" === u) {
                        if ("inline" === s || "inline-block" === s) {
                            r = r.parentNode;
                            continue
                        }
                        g = v
                    }
                    g / v < .9 && (o += 1),
                    r = r.parentNode
                } else {
                    if ("absolute" === f || "fixed" === f) {
                        r = r.parentNode;
                        break
                    }
                    r = r.parentNode
                }
            }
            return r
        }
        function Je(e) {
            for (var t = null; e && e.parentNode && e.parentNode !== document.body; ) {
                if ("a" === e.parentNode.tagName.toLocaleLowerCase()) {
                    t = e.parentNode;
                    break
                }
                e = e.parentNode
            }
            return t
        }
        function Xe(e) {
            if (e) {
                var t = e.cloneNode(!0)
                  , n = (t || {}).children;
                if (n && n.length > 0)
                    for (var r = 0; r < n.length; r++) {
                        var o = n[r];
                        /\b(badge)\b/i.test(Ve(o)) && t.removeChild(o)
                    }
                return (t.innerText || t.title || t.defaultValue || "").replace(/(^[\s\u3000*]+)|([\s\u3000\uff1a:~-]+$)|([(\uff08]\d+[)\uff09])/gm, "")
            }
            return ""
        }
        function Ve(e) {
            return e ? "string" == typeof e.className ? e.className : e.getAttribute("class") || "" : ""
        }
        function $e(e, t, n) {
            if (void 0 === t && (t = void 0),
            void 0 === n && (n = void 0),
            !e)
                return {};
            if (t && "function" == typeof t) {
                var r = t(n);
                if (r)
                    return {
                        feature: r.feature,
                        text: r.text || "",
                        placeholder: r.placeholder || "",
                        target: r.target || e
                    }
            }
            var o = ""
              , i = ""
              , a = ""
              , c = e
              , u = (ze(e) || {
                cursor: "default"
            }).cursor;
            "pointer" === u && (o = "clickable");
            var s = We(e);
            do {
                e.getAttribute("data-spm-click") && (o = "custom");
                var f = e.getAttribute("data-xux-log") || e.getAttribute("data-autolog");
                if (f) {
                    var d = (0,
                    Ye.parse)(f);
                    if (o = d.feature || "custom",
                    i = d.text || "",
                    d.ignore)
                        return {
                            feature: "",
                            placeholder: a,
                            text: i,
                            target: e
                        };
                    if (i)
                        return {
                            feature: o,
                            placeholder: a,
                            text: i,
                            target: e
                        }
                }
                var l = e.getAttribute("role");
                l && ~["button", "checkbox", "link", "menuitem", "radio", "tab", "combobox", "search"].indexOf(l) && (o = l);
                var p = (e.tagName || "").toLocaleLowerCase();
                switch (p) {
                case "input":
                    "text" === (o = e.type) ? a = e.placeholder || "" : "button" === o || "submit" === o ? (i = i || e.value,
                    o = "button") : "password" === o && (a = e.placeholder || "");
                    break;
                case "button":
                    i = i || Xe(e),
                    o = p;
                    break;
                case "select":
                case "textarea":
                    a = e.placeholder || "",
                    o = p;
                    break;
                case "a":
                case "area":
                    i = i || Xe(e) || e.alt || e.href,
                    o = "link";
                    break;
                case "label":
                    var g = e.getElementsByTagName("input");
                    if (g[0]) {
                        var v = g[0].type;
                        "checkbox" !== v && "radio" !== v || (o = v,
                        i || i || Xe(e))
                    }
                    break;
                case "svg":
                case "icon":
                    "pointer" === u && (o = "icon-button",
                    i = Xe(e) || "ICON_BUTTON");
                    break;
                case "img":
                    i = i || Xe(e) || e.alt;
                    var m = Je(e);
                    m ? (i = i || Xe(m) || m.href,
                    o = "link") : "pointer" === u && (i = i || "ICON_BUTTON",
                    o = "icon-button")
                }
                if ("li" === p && /\b(page|pagination)\b/i.test(Ve(e)))
                    return {
                        feature: "pagination",
                        placeholder: a,
                        text: i,
                        target: c
                    };
                if (/\bicon\b/i.test(Ve(e)) && "pointer" === u)
                    return {
                        feature: "icon-button",
                        placeholder: a,
                        text: Xe(e) || "ICON_BUTTON",
                        target: e
                    };
                if (/\bradio\b/i.test(Ve(e)))
                    return {
                        feature: "radio",
                        placeholder: a,
                        text: Xe(e),
                        target: e
                    };
                if (/\b(datetime|date)\b/i.test(Ve(e)))
                    return {
                        feature: "date",
                        placeholder: a,
                        text: Xe(e),
                        target: e
                    };
                if (/\b(prev|next|btn|button)\b/i.test(Ve(e)) && /^(?!next).*/.test(Ve(e))) {
                    i = Xe(e);
                    var h = ze(e)
                      , y = ze(e);
                    if (i)
                        return {
                            feature: "button",
                            placeholder: a,
                            text: i,
                            target: e
                        };
                    if (h && h.content ? i = h.content : y && y.content && (i = y.content),
                    !i) {
                        var w = e.getElementsByTagName("svg")
                          , b = e.getElementsByTagName("img")
                          , _ = e.getElementsByTagName("icon");
                        (w.length || b.length || _.length) && (i = "ICON_BUTTON")
                    }
                    return {
                        feature: "icon-button",
                        placeholder: a,
                        text: i,
                        target: e
                    }
                }
                if (!o || "clickable" === o) {
                    var O = e.getElementsByTagName("select");
                    if (1 === O.length) {
                        var T = ze(O[0]);
                        "absolute" != T.position && "none" !== T.display || (o = "select",
                        e = O[0])
                    }
                }
                if (o && "clickable" !== o && "text" !== o)
                    return {
                        feature: o,
                        placeholder: a,
                        text: i,
                        target: e
                    };
                e.parentNode && e.parentNode !== e && (e = e.parentNode)
            } while (e && e !== document.body && e !== s && e.getAttribute);
            return {
                feature: o,
                placeholder: a,
                text: i,
                target: c
            }
        }
        function Qe(e) {
            var t = e.feature
              , n = e.placeholder
              , r = e.text
              , o = e.target
              , i = We(o);
            switch (t) {
            case "custom":
            case "button":
            case "menuitem":
            case "tab":
                r = Xe(o);
                break;
            case "clickable":
            case "link":
                do {
                    if (r = Xe(o))
                        break;
                    o.parentNode && o.parentNode !== o && (o = o.parentNode)
                } while (o !== document.body && o !== i && !r);
                break;
            default:
                var a = o
                  , c = null;
                do {
                    o.parentNode && o.parentNode !== o && (c = o,
                    o = o.parentNode);
                    var u = o.getElementsByTagName("label");
                    if (u.length > 1) {
                        if (c && c.previousElementSibling)
                            "label" === (s = c.previousElementSibling).tagName.toLocaleLowerCase() && (r = Xe(s) || "");
                        break
                    }
                    if (1 === u.length) {
                        var s;
                        r = Xe(s = u[0]) || "";
                        break
                    }
                } while (o !== document.body && o !== i && !r);
                r = r || n || Xe(a),
                o = a
            }
            e.text = r,
            e.target = o
        }
        function Ze(e) {
            if (!e)
                return "";
            for (var t = []; e.parentNode; ) {
                var n = (e.tagName || "").toLocaleLowerCase()
                  , r = e.id;
                if (r && e !== document.body && e !== document.documentElement)
                    return ['//*[@id="' + r + '"]'].concat(t).join("/");
                var o = Array.prototype.slice.apply(e.parentNode.childNodes).filter((function(e) {
                    return (e.tagName || "").toLocaleLowerCase() === n
                }
                ));
                o.length > 1 ? t.unshift(n + "[" + (o.indexOf(e) + 1) + "]") : t.unshift(n),
                e = e.parentNode
            }
            return "/" + t.join("/")
        }
        function et(e, t) {
            if (!e)
                return !1;
            var n = {
                block: "rgba(195, 220, 182, 0.6)",
                click: "rgba(255, 255, 0, 0.4)"
            };
            Ke[t] && clearTimeout(Ke[t]),
            Ke[t] = setTimeout((function() {
                var r = {
                    left: 0,
                    top: 0,
                    position: "absolute",
                    backgroundColor: n[t]
                }
                  , o = document.documentElement.scrollTop
                  , i = document.documentElement.scrollLeft
                  , a = e.getBoundingClientRect().top
                  , c = e.getBoundingClientRect().left
                  , u = ze(e).width
                  , s = ze(e).height
                  , f = ze(e).position;
                "fixed" === f ? (r.top = a + "px",
                r.left = c + "px",
                r.position = f) : (r.top = a + o + "px",
                r.left = c + i + "px"),
                r.width = u,
                r.height = s;
                var d = document.createElement("div");
                He()(r).forEach((function(e) {
                    var t;
                    d.style[(t = e,
                    t ? t.replace(/-\D/g, (function(e) {
                        return e.charAt(1).toUpperCase()
                    }
                    )) : "")] = r[e]
                }
                )),
                document.body.appendChild(d),
                setTimeout((function() {
                    document.body.removeChild(d)
                }
                ), 500)
            }
            ), 100)
        }
        var tt = {
            on: function(e, t, n, r, o) {
                return e.addEventListener ? (o = o || !1,
                e.addEventListener(t, (function i(a) {
                    r && e.removeEventListener(t, i, o),
                    n.call(this, a)
                }
                ), o)) : e.attachEvent && e.attachEvent("on" + t, (function o(i) {
                    r && e.detachEvent("on" + t, o),
                    n.call(this, i)
                }
                )),
                this
            },
            shortenString: function(e, t) {
                return e ? e.substr(0, t) : ""
            },
            handleText: function(e) {
                return e ? (/^[+-]?[\d,]+(\.\d+)?$/.test(e) ? "666" : tt.shortenString(e, 500)) || "UNKNOWN" : ""
            },
            isDebug: function() {
                var e = window.location.search;
                return !(!e || !e.substring(1)) && "debug" === ((0,
                Ye.parse)(e.substring(1)) || {}).autolog
            }
        }
          , nt = tt
          , rt = ["target", "feature", "text"]
          , ot = function() {
            function e() {}
            var t = e.prototype;
            return t.wrapEvent = function() {
                var e = this;
                return function(t) {
                    var n = t.target;
                    if (n !== document && n !== document.documentElement) {
                        var r = $e(n, e.plugin, t);
                        if (r.feature) {
                            r.text || Qe(r);
                            var o = r.feature
                              , i = r.text
                              , a = r.target
                              , c = {
                                feature: o,
                                text: nt.handleText(i),
                                xpath: Ze(a),
                                selector: "",
                                logtype: "CLK"
                            }
                              , u = (0,
                            Ye.parse)(a.getAttribute("data-autolog") || "");
                            u && He()(u).forEach((function(e) {
                                "feature" !== e && "text" !== e && "xpath" !== e && "selector" !== e && "logtype" !== e && (c[e] = u[e])
                            }
                            )),
                            E.log("autolog", c),
                            nt.isDebug() && (et(a, "click"),
                            console.log(c));
                            var s = function(e) {
                                if (e)
                                    for (var t = e; t && t !== document.body && t.parentNode && t.parentNode.getAttribute; ) {
                                        t = t.parentNode;
                                        var n = (0,
                                        Ye.parse)(t.getAttribute("data-autolog") || "");
                                        if (n.feature && "block" === n.feature)
                                            return {
                                                feature: "block-click",
                                                text: n.text || "",
                                                target: t
                                            }
                                    }
                                return null
                            }(a);
                            if (s) {
                                var f = {
                                    feature: s.feature,
                                    text: s.text,
                                    xpath: Ze(s.target),
                                    selector: "",
                                    logtype: "CLK"
                                };
                                E.log("autolog", f),
                                nt.isDebug() && (et(s.target, "block"),
                                console.log(f))
                            }
                        }
                    }
                }
            }
            ,
            t.run = function() {
                if (window.getComputedStyle) {
                    var e = this.wrapEvent();
                    if ("ontouchstart"in window) {
                        var t = null
                          , n = 0;
                        nt.on(document, "touchstart", (function(e) {
                            var r = e.changedTouches;
                            r && 1 === r.length && (t = {
                                x: r[0].pageX,
                                y: r[0].pageY
                            },
                            n = Be()())
                        }
                        )),
                        nt.on(document, "touchend", (function(r) {
                            var o = r.changedTouches;
                            if (t && o && 1 === o.length) {
                                var i = {
                                    x: o[0].pageX,
                                    y: o[0].pageY
                                };
                                Math.pow(t.x - i.x, 2) + Math.pow(t.y - i.y, 2) < 100 && Be()() - n < 1e3 && e(r)
                            }
                            t = null
                        }
                        ))
                    } else
                        nt.on(document, "mousedown", e)
                }
            }
            ,
            t.autolog = function(e) {
                void 0 === e && (e = {});
                var t = e
                  , n = t.target
                  , r = t.feature
                  , o = t.text
                  , i = function(e, t) {
                    if (null == e)
                        return {};
                    var n, r, o = {}, i = Ge(e);
                    for (r = 0; r < i.length; r++)
                        n = i[r],
                        t.indexOf(n) >= 0 || (o[n] = e[n]);
                    return o
                }(t, rt);
                if (!n)
                    return console.error('Parameter "target" is required!'),
                    !1;
                var a = $e(n)
                  , c = a.feature
                  , u = a.text;
                if (r || c) {
                    var s = Fe({
                        feature: r || c,
                        text: nt.handleText(o || u || Qe(a)),
                        xpath: Ze(n),
                        selector: "",
                        logtype: "CLK"
                    }, i)
                      , f = (0,
                    Ye.parse)(n.getAttribute("data-autolog") || "");
                    f && He()(f).forEach((function(e) {
                        "feature" === e || "text" === e || "xpath" === e || "selector" === e || "logtype" === e || s[e] || (s[e] = f[e])
                    }
                    )),
                    E.log("autolog", s),
                    nt.isDebug() && console.log(s)
                }
            }
            ,
            t.setPlugin = function(e) {
                this.plugin = e
            }
            ,
            be(e)
        }()
          , it = n(5245)
          , at = n.n(it)
          , ct = at()({
            START_LOAD_TO_AUTOLOG: "START_LOAD_TO_AUTOLOG",
            IN_AEM_CONTAINER: "IN_AEM_CONTAINER",
            PLUGIN_START: "PLUGIN_START",
            START_LOAD_TO_AUTOLOG_FROM_PLUGIN: "START_LOAD_TO_AUTOLOG_FROM_PLUGIN"
        })
          , ut = at()({
            READY_TO_LOAD_BY_AUTOLOG: "READY_TO_LOAD_BY_AUTOLOG",
            READY_TO_LOAD_BY_AUTOLOG_TO_PLUGIN: "READY_TO_LOAD_BY_AUTOLOG_TO_PLUGIN"
        })
          , st = function(e) {
            return "string" == typeof e && /^https:\/\/(dev\.)?g\.alicdn\.com\/aes\/tracker-plugin-adata\//.test(e)
        }
          , ft = function(e) {
            var t = e.self
              , n = e.target
              , r = e.onMessage
              , o = function(e, t, n) {
                var r = function(e) {
                    e.data && "object" == typeof e.data && 1 === e.data._aes_adata_msg_flag_ && setTimeout((function() {
                        n(e.data, e)
                    }
                    ), 0)
                };
                return e.addEventListener("message", r, !1),
                {
                    send: function(e, n) {
                        var r = "function" == typeof t ? t() : t;
                        r && r.postMessage(Fe({}, e, {
                            _aes_adata_msg_flag_: 1
                        }), n || "*")
                    },
                    destroy: function() {
                        e.removeEventListener("message", r, !1)
                    }
                }
            }(t, n, (function(e, t) {
                console.log("IFrame \u6536\u5230\u6d88\u606f", e),
                r(e, t)
            }
            ))
              , i = o.send;
            return {
                send: function(e, t) {
                    console.log("\u4ece IFrame \u5411 MainFrame \u53d1\u9001\u6d88\u606f", e),
                    i(e, t)
                },
                destroy: o.destroy
            }
        };
        var dt = new ot;
        dt.run(),
        function() {
            try {
                if (window.parent && window !== window.parent) {
                    window._aes_autolog_adata_loader_ = !0;
                    var e = ft({
                        self: window,
                        target: window.parent,
                        onMessage: function(t, n) {
                            if (t.type === ct.IN_AEM_CONTAINER)
                                e && e.send({
                                    type: ut.READY_TO_LOAD_BY_AUTOLOG
                                }, n && n.origin);
                            else if (t.type === ct.START_LOAD_TO_AUTOLOG) {
                                var r = t.payload && t.payload.adataScriptUrl;
                                if (r && st(r)) {
                                    var o = document.createElement("script");
                                    o.src = r,
                                    document.body.appendChild(o)
                                }
                                e && e.destroy(),
                                e = null
                            }
                        }
                    })
                }
            } catch (e) {
                console.error(e)
            }
        }(),
        function() {
            try {
                var e = ft({
                    self: window,
                    target: function() {
                        var e = document.getElementById("aesAdataPluginIframe");
                        return e && e.contentWindow
                    },
                    onMessage: function(t, n) {
                        if (t.type === ct.PLUGIN_START)
                            e && e.send({
                                type: ut.READY_TO_LOAD_BY_AUTOLOG_TO_PLUGIN
                            }, n && n.origin);
                        else if (t.type === ct.START_LOAD_TO_AUTOLOG_FROM_PLUGIN) {
                            if (window._aes_autolog_adata_plugin_loader_)
                                return void console.log("\u5df2\u52a0\u8f7dadata plugin-render");
                            var r = t.payload && t.payload.adataScriptUrl;
                            if (r && st(r)) {
                                window._aes_autolog_adata_plugin_loader_ = !0;
                                var o = document.createElement("script");
                                o.src = r,
                                document.body.appendChild(o)
                            }
                            e && e.destroy(),
                            e = null
                        }
                    }
                })
                  , t = ft({
                    self: window,
                    target: window,
                    onMessage: function(e, n) {
                        "AES_ADATA_PLUGIN_LOAD" === e.type && (t && t.send({
                            type: "HAS_AES_AUTOLOG_TO_PLUGIN"
                        }, n && n.origin),
                        t && t.destroy(),
                        t = null)
                    }
                })
            } catch (e) {
                console.error(e)
            }
        }();
        var lt = function(e) {
            for (var t = [], n = window, r = document, o = r.body, i = 0, a = e.length; i < a; i++) {
                var c = e[i];
                if (c === o || c === r || c === n)
                    break;
                if (c.id) {
                    t.push("#".concat(c.id));
                    break
                }
                c.className && "string" == typeof c.className ? t.push("." + c.className.split(/\s+/).filter((function(e) {
                    return !!e
                }
                )).join(".")) : t.push(c.nodeName)
            }
            return t.reverse().join(" ")
        };
        function pt(e) {
            if ("[object Array]" === Object.prototype.toString.apply(e))
                return lt(e);
            for (var t = [], n = e; n; )
                t.push(n),
                n = n.parentNode;
            return lt(t)
        }
        function gt(e, t) {
            "function" == typeof requestIdleCallback ? requestIdleCallback(e, {
                timeout: t || 1e3
            }) : setTimeout(e, 0)
        }
        var vt = function(e) {
            return e.reduce((function(e, t) {
                return e + t
            }
            ), 0) / e.length
        }
          , mt = 1e3 / 60
          , ht = window.requestAnimationFrame || window.webkitRequestAnimationFrame
          , yt = window.cancelAnimationFrame || window.webkitCancelAnimationFrame
          , wt = {}
          , bt = function(e, t) {
            var n;
            ht && !wt[e] && (wt[e] = ht((function r() {
                var o = window.performance && performance.now ? performance.now() : (new Date).getTime();
                if (!n)
                    return n = o,
                    void (wt[e] = ht(r));
                t && t(o - n),
                n = o,
                wt[e] = ht(r)
            }
            )))
        };
        document.addEventListener("transitionstart", (function(e) {
            if (e && e.target && e.path) {
                var t = e.target;
                if (!t.__aesAnimationOnce) {
                    var n;
                    t.__aesAnimationOnce = 1;
                    var r = Math.random()
                      , o = (new Date).getTime()
                      , i = e.propertyName
                      , a = [];
                    bt(r, (function(e) {
                        a.length > 1e3 && a.shift(),
                        a.push(e)
                    }
                    ));
                    var c = function() {
                        var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                        t && t.removeEventListener("transitionend", n),
                        wt[r] && yt(wt[r]),
                        delete wt[r],
                        a.length && gt((function() {
                            var n = pt(e.path || t)
                              , r = isNaN(e.elapsedTime) ? (new Date).getTime() - o : 1e3 * e.elapsedTime
                              , c = Math.floor(r / mt);
                            E.log("animFluency", {
                                xpath: n,
                                animType: "transition",
                                animName: i,
                                rate: (c - a.length) / c,
                                fps: 1e3 / vt(a)
                            })
                        }
                        ))
                    }
                      , u = setTimeout((function() {
                        c()
                    }
                    ), 1100);
                    t && t.addEventListener && t.addEventListener("transitionend", n = function(e) {
                        clearTimeout(u),
                        c(e)
                    }
                    )
                }
            }
        }
        )),
        document.addEventListener("animationstart", (function(e) {
            if (e && e.target && e.path) {
                var t = e.target;
                if (!t.__aesAnimationOnce) {
                    var n;
                    t.__aesAnimationOnce = 1;
                    var r = Math.random()
                      , o = (new Date).getTime()
                      , i = e.animationName
                      , a = [];
                    bt(r, (function(e) {
                        a.length > 1e3 && a.shift(),
                        a.push(e)
                    }
                    ));
                    var c = function() {
                        var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                        t && t.removeEventListener("animationend", n),
                        wt[r] && yt(wt[r]),
                        delete wt[r],
                        a.length && gt((function() {
                            var n = pt(e.path || t)
                              , r = isNaN(e.elapsedTime) ? (new Date).getTime() - o : 1e3 * e.elapsedTime
                              , c = Math.floor(r / mt);
                            E.log("animFluency", {
                                xpath: n,
                                animType: "animation",
                                animName: i,
                                rate: (c - a.length) / c,
                                fps: 1e3 / vt(a)
                            })
                        }
                        ))
                    }
                      , u = setTimeout((function() {
                        c()
                    }
                    ), 1100);
                    t && t.addEventListener && t.addEventListener("animationend", n = function(e) {
                        clearTimeout(u),
                        c(e)
                    }
                    )
                }
            }
        }
        ));
        var _t = void 0 !== document.hidden ? {
            hidden: "hidden",
            visibilityChange: "visibilitychange"
        } : void 0 !== document.webkitHidden ? {
            hidden: "webkitHidden",
            visibilityChange: "webkitvisibilitychange"
        } : void 0 !== document.msHidden ? {
            hidden: "msHidden",
            visibilityChange: "msvisibilitychange"
        } : void 0
          , Ot = !!_t;
        !function() {
            if (window.PerformanceTouchScrollLatencyTiming) {
                var e, t = 0, n = 0;
                new PerformanceObserver((function(e) {
                    e.getEntries().forEach((function(e) {
                        n++,
                        e.duration > 100 && (t++,
                        E.log("tsl", {
                            name: e.name,
                            startTime: e.startTime,
                            duration: e.duration,
                            scrollTimes: n,
                            latencyTimes: t
                        }))
                    }
                    ))
                }
                )).observe({
                    entryTypes: ["touchscrolllatency"]
                }),
                function(e, t) {
                    var n;
                    Ot && document.addEventListener(_t.visibilityChange, n = function() {
                        t && document.removeEventListener(_t.visibilityChange, n),
                        e(!document[_t.hidden])
                    }
                    )
                }((function(r) {
                    !r && n > 0 && e !== n && (E.log("tsl", {
                        scrollTimes: n,
                        latencyTimes: t
                    }),
                    e = n)
                }
                ))
            }
        }();
        var Tt;
        ["pointerdown", "touchstart", "mousedown", "keydown", "mouseover"].forEach((function(e) {
            document.addEventListener(e, (function(e) {
                Tt = e
            }
            ), {
                capture: !0,
                passive: !0
            })
        }
        ));
        var xt = function(e) {
            for (var t = [], n = window, r = document, o = 0, i = e.length; o < i; o++) {
                var a = e[o];
                if (a === n || a === r)
                    break;
                if (a.id) {
                    t.push("#".concat(a.id));
                    break
                }
                a.className && "string" == typeof a.className ? t.push("." + a.className.split(/\s+/).filter((function(e) {
                    return !!e
                }
                )).join(".")) : t.push(a.nodeName)
            }
            return t.reverse().join(" ")
        };
        function Et(e) {
            if ("[object Array]" === Object.prototype.toString.apply(e))
                return xt(e);
            for (var t = [], n = e; n; )
                t.push(n),
                n = n.parentNode;
            return xt(t)
        }
        var At = void 0 !== document.hidden ? {
            hidden: "hidden",
            visibilityChange: "visibilitychange"
        } : void 0 !== document.webkitHidden ? {
            hidden: "webkitHidden",
            visibilityChange: "webkitvisibilitychange"
        } : void 0 !== document.msHidden ? {
            hidden: "msHidden",
            visibilityChange: "msvisibilitychange"
        } : void 0
          , Nt = !!At;
        !function() {
            if (window.PerformanceLongTaskTiming) {
                var e = new PerformanceObserver((function(e) {
                    e.getEntries().forEach((function(e) {
                        var t = Tt;
                        !function(e, t) {
                            "function" == typeof requestIdleCallback ? requestIdleCallback(e, {
                                timeout: t || 1e3
                            }) : setTimeout(e, 0)
                        }((function() {
                            E.log("longtask", {
                                startTime: e.startTime,
                                duration: e.duration,
                                xpath: t ? Et(t.path || t.target) : ""
                            })
                        }
                        ))
                    }
                    ))
                }
                ));
                e.observe({
                    entryTypes: ["longtask"]
                }),
                function(e, t) {
                    var n;
                    Nt && document.addEventListener(At.visibilityChange, n = function() {
                        t && document.removeEventListener(At.visibilityChange, n),
                        e(!document[At.hidden])
                    }
                    )
                }((function(t) {
                    t ? setTimeout((function() {
                        e.observe({
                            entryTypes: ["longtask"]
                        })
                    }
                    ), 100) : e.disconnect()
                }
                ))
            }
        }();
        var St = ["ec", "ea", "el", "et"];
        var Lt, kt = function(e, t) {
            var n = function(e) {
                var n = e.ec
                  , r = e.ea
                  , o = e.el
                  , i = e.et
                  , a = void 0 === i ? "CLK" : i
                  , c = e.xpath;
                delete e.ec,
                delete e.ea,
                delete e.el,
                delete e.et,
                delete e.xpath,
                e.p1 = n,
                e.p2 = r,
                e.p3 = o,
                e.p4 = a,
                e.p5 = c;
                try {
                    t.log("event", e)
                } catch (e) {}
            };
            return function() {
                var t = arguments
                  , r = {};
                if (0 !== t.length) {
                    for (var o = 0; o < t.length; o++) {
                        var i, a, c = t[o];
                        if (0 !== o && "object" == typeof c && o !== t.length - 1)
                            return void (null == e || null === (i = e.console) || void 0 === i || null === (a = i.warn) || void 0 === a || a.call(i, "[AES tracker-plugin-event]", "Only the last argument can be object type"));
                        if ("string" == typeof c || "number" == typeof c)
                            r[St[o]] = c;
                        else if ("object" == typeof c && o === t.length - 1)
                            for (var u in c)
                                c.hasOwnProperty(u) && (r[u] = c[u])
                    }
                    n(r)
                } else {
                    var s, f;
                    null === (s = e.console) || void 0 === s || null === (f = s.warn) || void 0 === f || f.call(s, "[AES tracker-plugin-event]", "At lease one augument")
                }
            }
        }, Ct = (Lt = window,
        kt(Lt, E)), jt = function(e) {
            for (var t = window.location.search.substring(1).split("&"), n = 0; n < t.length; n++) {
                var r = t[n].split("=");
                if (r[0] === e)
                    return r[1]
            }
            return !1
        }, It = function(e, t, n) {
            if (!e || !Array.isArray(t) || 0 == t.length)
                return e || n;
            var r = t[0]
              , o = t.slice(1);
            return It(e[r], o, n)
        }, Pt = function() {
            var e;
            "1" === jt("_debugConsole_") && (e = console).info.apply(e, arguments)
        };
        !function() {
            try {
                if (location.href.includes("alibaba-inc") || "true" === jt("__isGray__") || "wapa" === jt("__mtop_subdomain__") || "pre" === jt("_env_") || "debug" === jt("env") || window.__isSSR || window.__server__ || window.__disableAEM__)
                    return;
                var e = jt("__pageId__") || It(window, ["$$pageSchema", "attributes", "id"]) || window.__aemPageId__;
                Pt("pageId", e);
                var t = "pc_rax" === It(window, ["$$pageSchema", "attributes", "client"]) ? "zgc-" + e + "-pc" : "zgc-" + e;
                if (e && (E.setConfig({
                    pid: t,
                    user_type: "3",
                    uid: "",
                    username: ""
                }),
                window.AES_CONFIG = window.AES_CONFIG || {},
                window.AES_CONFIG.pid = t,
                window.AES_CONFIG.user_type = "3",
                window.AES_CONFIG.uid = "",
                window.AES_CONFIG.username = ""),
                window.aesRecord = Ct,
                Pt("__aemSelector__", window.__aemSelector__),
                window.__aemSelector__) {
                    var n = function(e) {
                        e > 15e3 || e < 0 || (Pt("first-print", e),
                        Ct("FS", {
                            et: "EXP",
                            c6: e
                        }))
                    }
                      , r = (o = function() {
                        document.querySelector("body " + window.__aemSelector__) && (Te("FMP"),
                        n((new Date).getTime() - performance.timing.navigationStart),
                        document.removeEventListener("DOMNodeInserted", r))
                    }
                    ,
                    i = 10,
                    a = Date.now(),
                    function() {
                        var e = Date.now();
                        e - a >= i && (o(),
                        a = e)
                    }
                    );
                    if (document.querySelector("body " + window.__aemSelector__))
                        return Te("FMP"),
                        void n((new Date).getTime() - performance.timing.navigationStart);
                    document.addEventListener("DOMNodeInserted", r),
                    setTimeout((function() {
                        document.removeEventListener("DOMNodeInserted", r)
                    }
                    ), 15e3)
                }
            } catch (e) {
                console.warn(e.message)
            }
            var o, i, a
        }()
    }()
}();
var feloader = function(t) {
    !function(t) {
        "use strict";
        for (var e, r, n = {}, i = function() {}, o = "memory".split(","), a = "assert,clear,count,debug,dir,dirxml,error,exception,group,groupCollapsed,groupEnd,info,log,markTimeline,profile,profiles,profileEnd,show,table,time,timeEnd,timeline,timelineEnd,timeStamp,trace,warn".split(","); e = o.pop(); )
            t[e] = t[e] || n;
        for (; r = a.pop(); )
            t[r] = t[r] || i
    }(this.console = this.console || {});
    var e = this
      , r = function() {
        this.Env = {
            host: e,
            mods: {}
        },
        this.Config = {
            debug: "",
            packages: {},
            fns: {},
            useDailyAssets: !1,
            forceAssetsHost: t,
            assetsHost: "g.alicdn.com",
            dailyAssetsHost: "dev.g.alicdn.com",
            crossorigin: !1
        };
        var r = this.Loader = {};
        r.Status = {
            ERROR: -1,
            UNLOADED: 0,
            LOADING: 1,
            LOADED: 2,
            INITIALIZING: 3,
            INITIALIZED: 4
        },
        this.initUtils(),
        this.initDataStructure(),
        this.initCssOnLoad(),
        this.initGetScript(),
        this.initConfig(),
        this.initComboLoader(),
        this.initLoader(),
        this.init()
    };
    return r.prototype.__BUILD_TIME = "",
    r.prototype.version = "5.0.8",
    r.prototype.config = function(e, r) {
        var n, i, o, a = this.Config, s = a.fns, u = this;
        if ("string" == typeof e)
            n = s[e],
            r === t ? i = n ? n.call(u) : a[e] : n ? i = n.call(u, r) : a[e] = r;
        else
            for (var c in e)
                r = e[c],
                o = s[c],
                o ? o.call(u, r) : a[c] = r;
        return i
    }
    ,
    r
}();
!function(t) {
    function e(t) {
        var e = t.match(u) || []
          , r = {};
        for (var n in c)
            r[n] = e[c[n]];
        return r.hostname && (r.hostname = r.hostname.toLowerCase()),
        r.hostname && !r.pathname && (r.pathname = "/"),
        r.host = r.hostname,
        r.port && (r.host = r.hostname + ":" + r.port),
        r
    }
    function r(t) {
        var e = 0;
        return parseFloat(t.replace(/\./g, function() {
            return 0 === e++ ? "." : ""
        }))
    }
    function n(t) {
        var e = t.split(/\//);
        return "/" === t.charAt(0) && e[0] && e.unshift(""),
        "/" === t.charAt(t.length - 1) && t.length > 1 && e[e.length - 1] && e.push(""),
        e
    }
    function i(t, e) {
        var r, n, i = 0;
        if (l(t))
            for (n = t.length; n > i && e(t[i], i, t) !== !1; i++)
                ;
        else
            for (r = o(t),
            n = r.length; n > i && e(t[r[i]], r[i], t) !== !1; i++)
                ;
    }
    function o(t) {
        var e = [];
        for (var r in t)
            e.push(r);
        return e
    }
    function a(t, e) {
        for (var r in e)
            t[r] = e[r];
        return t
    }
    function s(t) {
        return "/" === t.charAt(0) && (t = 0 === t.indexOf("//") ? location.protocol + t : location.protocol + "//" + location.host + t),
        "/" === t.charAt(t.length - 1) && (t += "index"),
        p.endsWith(t, ".js") && (t = t.slice(0, -3)),
        t
    }
    var u = new RegExp("^([\\w\\d+.-]+:)?(?://(?:([^/?#@]*)@)?([\\w\\d\\-\\u0100-\\uffff.+%]*|\\[[^\\]]+\\])(?::([0-9]+))?)?([^?#]+)?(\\?[^#]*)?(#.*)?$")
      , c = {
        protocol: 1,
        auth: 2,
        hostname: 3,
        port: 4,
        pathname: 5,
        search: 6,
        hash: 7
    }
      , l = Array.isArray || function(t) {
        return "[object Array]" === Object.prototype.toString.call(t)
    }
      , f = /(http(s)?:)?\/\/([^\/]+)(?::(\d+))?/
      , d = Array.prototype.map
      , h = Array.prototype.filter
      , g = String.prototype.startsWith
      , p = {
        noop: function() {},
        filter: h ? function(t, e, r) {
            return d.call(t, e, r || this)
        }
        : function(t, e, r) {
            for (var n = t.length, i = new Array(n), o = 0; n > o; o++) {
                var a = "string" == typeof t ? t.charAt(o) : t[o];
                (a || o in t) && e.call(r || this, a, o, t) && i.push(a)
            }
            return i
        }
        ,
        map: d ? function(t, e, r) {
            return d.call(t, e, r || this)
        }
        : function(t, e, r) {
            for (var n = t.length, i = new Array(n), o = 0; n > o; o++) {
                var a = "string" == typeof t ? t.charAt(o) : t[o];
                (a || o in t) && (i[o] = e.call(r || this, a, o, t))
            }
            return i
        }
        ,
        startsWith: g ? function(t, e) {
            return g.call(t, e)
        }
        : function(t, e) {
            return 0 === t.lastIndexOf(e, 0)
        }
        ,
        isEmptyObject: function(t) {
            for (var e in t)
                if (void 0 !== e)
                    return !1;
            return !0
        },
        endsWith: function(t, e) {
            var r = t.length - e.length;
            return r >= 0 && t.indexOf(e, r) === r
        },
        now: Date.now || function() {
            return +new Date
        }
        ,
        each: i,
        keys: o,
        isArray: l,
        indexOf: function(t, e) {
            for (var r = 0, n = e.length; n > r; r++)
                if (e[r] === t)
                    return r;
            return -1
        },
        normalizeSlash: function(t) {
            return t.replace(/\\/g, "/")
        },
        normalizePath: function(t, r) {
            var i = r.charAt(0);
            if ("." !== i)
                return r;
            var o = "";
            if (p.startsWithProtocol(t)) {
                var a = e(t);
                o = a.protocol + "//" + a.host,
                t = a.pathname
            }
            var s = n(t)
              , u = n(r);
            s.pop();
            for (var c = 0, l = u.length; l > c; c++) {
                var f = u[c];
                "." === f || (".." === f ? s.pop() : s.push(f))
            }
            return o + s.join("/").replace(/\/+/, "/")
        },
        startsWithProtocol: function(t) {
            return p.startsWith(t, "http:") || p.startsWith(t, "https:") || p.startsWith(t, "file:")
        },
        isSameOriginAs: function(t, e) {
            var r = t.match(f)
              , n = e.match(f);
            return r[0] === n[0]
        },
        getHash: function(t) {
            var e, r = 5381;
            for (e = t.length; --e > -1; )
                r = (r << 5) + r + t.charCodeAt(e);
            return r + ""
        },
        getSuffix: function(t) {
            var e = t.match(/\.(\w+)$/);
            return e ? e[1] : void 0
        }
    }
      , m = function() {
        var t, e, n = this.Loader, i = this.Env, o = n.Status, u = i.mods, c = i.host, l = n.Utils = {}, f = c.document, d = (c.navigator || {}).userAgent || "";
        ((t = d.match(/Web[Kk]it[\/]{0,1}([\d.]*)/)) || (t = d.match(/Safari[\/]{0,1}([\d.]*)/))) && t[1] && (l.webkit = r(t[1])),
        (t = d.match(/Trident\/([\d.]*)/)) && (l.trident = r(t[1])),
        (t = d.match(/Gecko/)) && (l.gecko = .1,
        (t = d.match(/rv:([\d.]*)/)) && t[1] && (l.gecko = r(t[1]))),
        (t = d.match(/MSIE ([^;]*)|Trident.*; rv(?:\s|:)?([0-9.]+)/)) && (e = t[1] || t[2]) && (l.ie = r(e),
        l.ieMode = f.documentMode || l.ie,
        l.trident = l.trident || 1),
        a(l, p),
        a(l, {
            mix: a,
            docHead: function() {
                return f.getElementsByTagName("head")[0] || f.documentElement
            },
            collectErrors: function(t, e, r) {
                var n, i, a, s;
                for (r = r || {},
                e = e || [],
                n = 0; n < t.length; n++)
                    a = t[n],
                    i = a.id,
                    r[i] || (r[i] = 1,
                    s = a.status,
                    s !== o.ERROR ? l.collectErrors(a.getNormalizedRequiredModules(), e, r) : e.push(a));
                return e
            },
            createModule: function(t, e) {
                t = s(t);
                var r = u[t];
                return r || (r = u[t]),
                r ? (e && r.reset(e),
                r) : (u[t] = r = new n.Module(a({
                    id: t
                }, e)),
                r)
            },
            createModules: function(t) {
                return l.map(t, function(t) {
                    return l.createModule(t)
                })
            },
            initModules: function(t) {
                var e, r = t.length, n = 1;
                for (e = 0; r > e; e++)
                    n &= t[e].initRecursive();
                return n
            },
            getModulesExports: function(t) {
                for (var e = t.length, r = [], n = 0; e > n; n++)
                    r.push(t[n].getExports());
                return r
            },
            addModule: function(t, e, r) {
                var n = u[t];
                return n && void 0 !== n.factory ? (console.warn(t + " is defined more than once"),
                void 0) : (l.createModule(t, a({
                    id: t,
                    status: o.LOADED,
                    factory: e
                }, r)),
                void 0)
            }
        })
    };
    t.prototype.initUtils = m
}(feloader),
function(t, e) {
    function r(t, r) {
        var n = this;
        n.name = e,
        n.base = e,
        n.main = e,
        n.filter = e,
        n.tag = e,
        n.charset = e,
        n.combine = e,
        n.group = e,
        n.modules = {},
        n.ctx = r,
        n.ctx.Loader.Utils.mix(n, t)
    }
    function n(t, r) {
        return t[r] !== e ? t[r] : t.ctx.Config[r]
    }
    function i(t, e, r) {
        for (var n = 0; n < e.length; n++)
            e[n] = t.resolve(e[n]).id;
        t.ctx.use(e, r)
    }
    function o(t, r) {
        var n = this;
        n.ctx = r;
        var o = this.ctx.Loader.Status
          , a = this.ctx.Loader.Utils;
        n.exports = e,
        n.module = n,
        n.status = o.UNLOADED,
        n.id = e,
        n.factory = e,
        n.config = e,
        n.cjs = 1;
        var s = this.ctx.Loader.Utils.mix;
        s(n, t),
        n.waits = {};
        var u = n._require = function(t, e) {
            if ("string" == typeof t) {
                var r = n.resolve(t);
                return a.initModules(r.getNormalizedModules()),
                r.getExports()
            }
            i(n, t, e)
        }
        ;
        u.toUrl = function(t) {
            var e = n.getUri()
              , r = ""
              , i = e
              , o = e.indexOf("//");
            return -1 !== o && (r = e.slice(0, o + 2),
            i = e.slice(o + 2)),
            r + a.normalizePath(i, t)
        }
        ,
        u.load = r.getScript
    }
    function a(e, r) {
        var n = e.indexOf("!");
        if (-1 !== n) {
            var i = e.substring(0, n);
            e = e.substring(n + 1);
            var o = r.ctx.Loader.Utils.createModule(i);
            o.initRecursive();
            var a = o.getExports() || {};
            a.alias && (e = a.alias(t, e, i))
        }
        return e
    }
    function s(t, e) {
        t = t || [];
        for (var r = t.length, n = 0; r > n; n++)
            t[n] = e.resolve(t[n]).id;
        return t
    }
    function u(t) {
        var e, r = t.id, n = t.alias;
        if ("string" == typeof n && (t.alias = n = [n]),
        n)
            return n;
        if (e = t.getPackage()) {
            var i;
            e.name === r && (i = e.main) ? (r += "/",
            "." !== i.charAt(0) && (i = "./" + i),
            n = [t.ctx.Loader.Utils.normalizePath(r, i)]) : e.alias && (n = e.alias(r))
        }
        return n = t.alias = n || [a(r, t)]
    }
    var c = "ignorePackageNameInUri";
    r.prototype = {
        constructor: r,
        reset: function(t) {
            this.ctx.Loader.Utils.mix(this, t);
            for (var e in this.modules)
                this.modules[e].reset()
        },
        getFilter: function() {
            return n(this, "filter")
        },
        getTag: function() {
            return n(this, "tag")
        },
        getBase: function() {
            return this.base
        },
        getCharset: function() {
            return n(this, "charset")
        },
        isCombine: function() {
            return n(this, "combine")
        },
        isIgnorePackageNameInUri: function() {
            return n(this, c)
        },
        getGroup: function() {
            return n(this, "group")
        },
        addChildModule: function(t, e) {
            this.modules[t] = e
        }
    },
    o.prototype = {
        feloader: 1,
        constructor: o,
        config: function() {
            return this.config
        },
        reset: function(t) {
            var e = this
              , r = this.ctx.Loader.Utils.mix;
            r(e, t),
            t && t.requires && e.setRequiresModules(t.requires),
            delete e.packageInfo
        },
        require: function(t) {
            return this.resolve(t).getExports()
        },
        resolve: function(t) {
            var e = this.ctx.Loader.Utils;
            return e.createModule(e.normalizePath(this.id, t))
        },
        add: function(t) {
            this.waits[t.id] = t
        },
        remove: function(t) {
            delete this.waits[t.id]
        },
        contains: function(t) {
            return this.waits[t.id]
        },
        flush: function() {
            this.ctx.Loader.Utils.each(this.waits, function(t) {
                t.flush()
            }),
            this.waits = {}
        },
        getType: function() {
            var t = this.ctx.Loader.Utils
              , e = this
              , r = e.type;
            if (!r) {
                var n = e.id;
                r = t.endsWith(n, ".css") ? "css" : "js",
                e.type = r
            }
            return r
        },
        getAlias: function() {
            var t = this
              , e = t.id
              , r = u(t)
              , n = [];
            if (r[0] === e)
                n = r;
            else if (r.length > 1)
                for (var i = 0, o = r.length; o > i; i++) {
                    var a = r[i];
                    if (a && a !== e) {
                        var s = this.ctx.Loader.Utils.createModule(a)
                          , c = s.getAlias();
                        c ? n.push.apply(n, c) : n.push(a)
                    }
                }
            else
                n.push(r[0]);
            return t.normalizedAlias = n,
            n
        },
        getNormalizedModules: function() {
            var t = this
              , e = t.getAlias()
              , r = []
              , n = this.ctx.Loader.Utils;
            return n.each(e, function(t) {
                t && r.push(t)
            }),
            t.normalizedModules = n.map(r, function(e) {
                return t.ctx.Loader.Utils.createModule(e)
            }),
            t.normalizedModules
        },
        fixTwoVersion: function(t) {
            var e = /(\d+\.\d+\.\d+\/.*)\d+\.\d+\.\d+\//;
            return e.test(t) && (t = t.replace(e, "$1")),
            t
        },
        getUri: function() {
            var t = this;
            return t.uri = this.ctx.Loader.Utils.normalizeSlash(this.ctx.Config.resolveModFn(t)),
            this.fixTwoVersion(t.uri)
        },
        getUrl: function() {
            return this.getUri()
        },
        getExports: function() {
            var t = this.getNormalizedModules();
            return t[0] && t[0].exports
        },
        getPackage: function() {
            var t = this;
            if ("undefined" != typeof t.packageInfo)
                return t.packageInfo;
            var e = t.id
              , r = this.ctx.Config
              , n = this.ctx.Loader.Utils
              , i = n.startsWith
              , o = n.filter
              , a = r.packages
              , s = t.id + "/"
              , u = o(s.split("/"), function(t) {
                return t.length > 0
            }).slice(0, 2).join("/");
            if (a[u])
                return t.packageInfo = a[u],
                t.packageInfo;
            u = "";
            var c;
            for (c in a) {
                var l = c;
                n.endsWith(l, "/") || (l += "/"),
                i(s, l) && c.length > u.length && (u = c)
            }
            return a[u] ? (t.packageInfo = a[u],
            t.packageInfo.addChildModule(u, t),
            t.packageInfo) : i(e, "/") || i(e, "http://") || i(e, "https://") || i(e, "file://") ? (t.packageInfo = null,
            t.packageInfo) : (t.packageInfo = a.core,
            t.packageInfo)
        },
        getTag: function() {
            var t = this;
            return t.tag || t.getPackage() && t.getPackage().getTag()
        },
        getCharset: function() {
            var t = this;
            return t.charset || t.getPackage() && t.getPackage().getCharset()
        },
        setRequiresModules: function(t) {
            var e = this
              , r = e.requiredModules = e.ctx.Loader.Utils.map(s(t, e), function(t) {
                return e.ctx.Loader.Utils.createModule(t)
            })
              , n = [];
            this.ctx.Loader.Utils.each(r, function(t) {
                n.push.apply(n, t.getNormalizedModules())
            }),
            e.normalizedRequiredModules = n
        },
        getNormalizedRequiredModules: function() {
            var t = this;
            return t.setRequiresModules(t.requires),
            t.normalizedRequiredModules
        },
        getRequiredModules: function() {
            var t = this;
            return t.requiredModules ? t.requiredModules : (t.setRequiresModules(t.requires),
            t.requiredModules)
        },
        callFactory: function() {
            var t = this;
            return t.factory.apply(t, t.cjs ? [t._require, t.exports, t] : t.ctx.Loader.Utils.map(t.getRequiredModules(), function(t) {
                return t.getExports()
            }))
        },
        initSelf: function() {
            var t, r = this, n = r.factory, i = this.ctx.Config, o = this.ctx.Loader.Status, a = this.ctx.Loader.Utils;
            if ("function" == typeof n) {
                if (r.exports = {},
                i.debug)
                    t = r.callFactory();
                else {
                    try {
                        t = r.callFactory()
                    } catch (s) {
                        if (r.status = o.ERROR,
                        r.onError || i.onModuleError) {
                            var u = {
                                type: "init",
                                exception: s,
                                module: r
                            };
                            r.error = u,
                            r.onError && r.onError(u),
                            i.onModuleError && i.onModuleError(u)
                        } else
                            setTimeout(function() {
                                throw s
                            }, 0);
                        return 0
                    }
                    var c = 1;
                    if (a.each(r.getNormalizedRequiredModules(), function(t) {
                        return t.status === o.ERROR ? (c = 0,
                        !1) : void 0
                    }),
                    !c)
                        return 0
                }
                t !== e && (r.exports = t)
            } else
                r.exports = n;
            return r.status = o.INITIALIZED,
            r.afterInit && r.afterInit(r),
            i.afterModuleInit && i.afterModuleInit(r),
            1
        },
        initRecursive: function() {
            var t = this
              , e = 1
              , r = t.status
              , n = this.ctx.Loader.Status
              , i = this.ctx.Loader.Utils;
            return r === n.ERROR ? 0 : r >= n.INITIALIZING ? e : (t.status = n.INITIALIZING,
            t.cjs ? e = t.initSelf() : (i.each(t.getNormalizedRequiredModules(), function(t) {
                e = e && t.initRecursive()
            }),
            e && t.initSelf()),
            e)
        },
        undef: function() {
            this.status = this.ctx.Loader.Status.UNLOADED,
            this.error = null,
            this.factory = null,
            this.exports = null
        }
    };
    var l = function() {
        var t = this
          , e = this.Loader;
        e.Package = function(e) {
            return new r(e,t)
        }
        ,
        e.Module = function(e) {
            return new o(e,t)
        }
    };
    t.prototype.initDataStructure = l
}(feloader),
function(t) {
    var e = function() {
        function t() {
            o || r()
        }
        function e(t) {
            var e = 0;
            if (i.webkit)
                t.sheet && (e = 1);
            else if (t.sheet)
                try {
                    var r = t.sheet.cssRules;
                    r && (e = 1)
                } catch (n) {
                    var o = n.name;
                    "NS_ERROR_DOM_SECURITY_ERR" === o && (e = 1)
                }
            return e
        }
        function r() {
            for (var t in a) {
                var s = a[t]
                  , u = s.node;
                e(u) && (s.callback && s.callback.call(u),
                delete a[t])
            }
            o = i.isEmptyObject(a) ? 0 : setTimeout(r, n)
        }
        var n = 30
          , i = this.Loader.Utils
          , o = 0
          , a = {};
        i.pollCss = function(e, r) {
            var n = e.href
              , i = a[n] = {};
            i.node = e,
            i.callback = r,
            t()
        }
        ,
        i.isCssLoaded = e
    };
    t.prototype.initCssOnLoad = e
}(feloader),
function(t) {
    var e = function() {
        var t, e = 1e3, r = this.Env.host, n = r.document, i = this.Loader.Utils, o = this.Config, a = {}, s = i.webkit;
        this.getScript = function(r, u, c, l) {
            function f() {
                var t = M.readyState;
                t && "loaded" !== t && "complete" !== t || (M.onreadystatechange = M.onload = null,
                E(0))
            }
            var d, h, g, p, m, v = u, y = o.crossorigin, x = i.endsWith(r, ".css");
            if (l === !0 ? y = !0 : l === !1 && (y = !1),
            "object" == typeof v && (u = v.success,
            d = v.error,
            h = v.timeout,
            c = v.charset,
            g = v.attrs,
            v.crossorigin === !0 ? y = !0 : v.crossorigin === !1 && (y = !1)),
            x && i.ieMode < 10 && n.getElementsByTagName("style").length + n.getElementsByTagName("link").length >= 31)
                return setTimeout(function() {
                    throw new Error("style and link's number is more than 31.ie < 10 can not insert link: " + r)
                }, 0),
                d && d(),
                void 0;
            if (p = a[r] = a[r] || [],
            p.push([u, d]),
            p.length > 1)
                return p.node;
            var M = n.createElement(x ? "link" : "script")
              , b = function() {
                m && (clearTimeout(m),
                m = void 0)
            };
            g && i.each(g, function(t, e) {
                M.setAttribute(e, t)
            }),
            c && (M.charset = c),
            x ? (M.href = r,
            M.rel = "stylesheet") : (M.src = r,
            M.async = !0,
            y && M.setAttribute("crossorigin", "anonymous")),
            p.node = M;
            var E = function(t) {
                var e, n = t;
                b(),
                i.each(a[r], function(t) {
                    (e = t[n]) && e.call(M)
                }),
                delete a[r]
            }
              , L = "onload"in M
              , k = o.forceCssPoll || s && 536 > s || !s && !i.trident && !i.gecko && !Object.assign;
            return x && k && L && (L = !1),
            L ? (M.onload = f,
            M.onerror = function() {
                M.onerror = null,
                E(1)
            }
            ) : x ? i.pollCss(M, function() {
                E(0)
            }) : M.onreadystatechange = f,
            h && (m = setTimeout(function() {
                E(1)
            }, h * e)),
            t || (t = i.docHead()),
            x ? t.appendChild(M) : t.insertBefore(M, t.firstChild),
            M
        }
    };
    t.prototype.initGetScript = e
}(feloader),
function(t, e) {
    function r(t, e) {
        return function(r) {
            var n = {};
            for (var i in r)
                n[i] = {},
                n[i][t] = r[i];
            e.config("modules", n)
        }
    }
    var n = function() {
        function t(t, e) {
            if (t = s.normalizeSlash(t),
            e && "/" !== t.charAt(t.length - 1) && (t += "/"),
            l) {
                if (s.startsWith(t, "http:") || s.startsWith(t, "//") || s.startsWith(t, "https:") || s.startsWith(t, "file:"))
                    return t;
                t = l.protocol + "//" + l.host + s.normalizePath(l.pathname, t)
            }
            return t
        }
        function n(t, e, r) {
            var n = e.getTag() || c.tag || "";
            return n && (r && (n += r),
            t += "?t=" + n),
            t
        }
        var i = this
          , o = this.Loader
          , a = o.Package
          , s = o.Utils
          , u = this.Env.host
          , c = this.Config
          , l = u.location
          , f = c.fns;
        c.loadModsFn = function(t, e) {
            i.getScript(t.uri, e)
        }
        ,
        c.resolveModFn = function(t) {
            var e, r, i, o, a = t.id, u = t.path, c = t.getPackage();
            if (!c) {
                var l = s.endsWith(a, ".css")
                  , f = s.endsWith(a, ".js");
                return o = l ? "css" : "js",
                i = "." + o,
                l || f || (a += ".js"),
                n(a, t, i)
            }
            var d = c.getBase()
              , h = c.name;
            return o = t.getType(),
            i = "." + o,
            u || (s.endsWith(a, i) && (a = a.slice(0, -i.length)),
            e = c.getFilter() || "",
            "function" == typeof e ? u = e(a, o) : "string" == typeof e && (e && (e = "-" + e),
            u = a + e + i)),
            "core" === h ? r = d + u : a === h ? r = d.substring(0, d.length - 1) + e + i : (c.isIgnorePackageNameInUri() && (u = u.substring(h.length + 1)),
            r = d + u),
            n(r, t, i)
        }
        ,
        f.requires = r("requires", i),
        f.alias = r("alias", i),
        f.packages = function(r) {
            var n = c.packages;
            return r === e ? n : r ? (s.each(r, function(e, r) {
                var i = e.name || r;
                s.startsWith(i, "/") ? i = l.protocol + "//" + l.host + i : (s.startsWith(i, "./") || s.startsWith(i, "../")) && (i = s.normalizePath(l.href, i)),
                s.endsWith(i, "/") && (i = i.slice(0, -1)),
                e.name = i;
                var o = e.base || e.path;
                o && (e.base = t(o, !0)),
                n[i] ? n[i].reset(e) : n[i] = new a(e)
            }),
            e) : (c.packages = {
                core: n.core
            },
            e)
        }
        ,
        f.modules = function(e) {
            e && s.each(e, function(e, r) {
                var n = e.uri;
                n && (e.uri = t(n)),
                s.createModule(r, e)
            })
        }
        ,
        f.base = function(t) {
            var r = this
              , n = c.packages.core;
            return t ? (r.config("packages", {
                core: {
                    base: t
                }
            }),
            e) : n && n.getBase()
        }
    };
    t.prototype.initConfig = n
}(feloader),
function(t, e) {
    function r(t, e) {
        if (t || "function" != typeof e)
            t && t.requires && !t.cjs && (t.cjs = 0);
        else {
            var r = [];
            r.length && (t = t || {},
            t.requires = r)
        }
        return t
    }
    function n(t) {
        var e, r, n, i = [];
        for (e = 0,
        n = t.length; n > e; e++)
            r = t[e],
            "exports" === r || "module" === r || "require" === r || i.push(r);
        return i
    }
    function i(t, e) {
        var r = t.indexOf("//")
          , n = "";
        -1 !== r && (n = t.substring(0, t.indexOf("//") + 2)),
        t = t.substring(n.length).split(/\//),
        e = e.substring(n.length).split(/\//);
        for (var i = Math.min(t.length, e.length), o = 0; i > o && t[o] === e[o]; o++)
            ;
        var a = n + t.slice(0, o).join("/") + "/";
        return a = a.replace(/\/\/$/, "/")
    }
    function o(t, e, r, n, i, o) {
        if (t && e.length > 1) {
            for (var a = t.length, s = [], u = 0; u < e.length; u++)
                s[u] = e[u].substring(a);
            return r + t + n + s.join(i) + o
        }
        return r + n + e.join(i) + o
    }
    var a = function() {
        function t(t, r, n) {
            function i() {
                --o || r(s, a)
            }
            var o = t && t.length
              , a = []
              , s = [];
            m(t, function(t) {
                var r, o = {
                    timeout: n,
                    success: function() {
                        s.push(t),
                        r && u && (p(r.id, u.factory, u.config),
                        u = e),
                        i()
                    },
                    error: function() {
                        a.push(t),
                        i()
                    },
                    charset: t.charset
                };
                t.combine || (r = t.mods[0],
                "css" === r.getType() ? r = e : b && (c = r.id,
                l = +new Date,
                o.attrs = {
                    "data-mod-id": r.id
                })),
                d.loadModsFn(t, o)
            })
        }
        function a(t) {
            this.callback = t,
            this.head = this.tail = e,
            this.id = "loader" + ++E
        }
        function s() {
            var t, e, r, n, i = document.getElementsByTagName("script");
            for (e = i.length - 1; e >= 0; e--)
                if (n = i[e],
                "interactive" === n.readyState) {
                    t = n;
                    break
                }
            return r = t ? t.getAttribute("data-mod-id") : c
        }
        var u, c, l, f = this.Loader, d = this.Config, h = f.Status, g = f.Utils, p = g.addModule, m = g.each, v = g.getHash, y = h.LOADING, x = h.LOADED, M = h.ERROR, b = g.ieMode && g.ieMode < 10, E = 0;
        a.add = function(t, i, o, a) {
            if ("string" == typeof t)
                if (3 === a && g.isArray(i)) {
                    var f = i;
                    i = o,
                    o = {
                        requires: n(f),
                        cjs: 1
                    }
                } else
                    2 === a && i.call && (o = {
                        cjs: 1
                    });
            if (g.isArray(t) && 2 === a) {
                var f = t;
                t = i,
                i = {
                    requires: n(f),
                    cjs: 1
                }
            }
            "function" == typeof t || 1 === a ? (o = i,
            i = t,
            o = r(o, i),
            b ? (t = s(),
            t && p(t, i, o),
            c = null,
            l = 0) : u = {
                factory: i,
                config: o
            }) : (b ? (c = null,
            l = 0) : u = e,
            o = r(o, i),
            p(t, i, o))
        }
        ;
        var L;
        L = function(t) {
            m(t, function(t) {
                var e = [];
                m(t.mods, function(t) {
                    t.status === x && e.push(t.id)
                })
            })
        }
        ,
        g.mix(a.prototype, {
            use: function(e) {
                for (var r, n = this, i = d.timeout, o = [], a = 0; a < e.length; a++)
                    e[a].id && o.push(e[a]);
                e = o,
                r = n.getComboUris(e),
                r.css && t(r.css, function(t, e) {
                    L(t),
                    m(t, function(t) {
                        m(t.mods, function(t) {
                            p(t.id, g.noop),
                            t.flush()
                        })
                    }),
                    m(e, function(t) {
                        m(t.mods, function(e) {
                            var r = e.id + " is not loaded! can not find module in uri: " + t.uri;
                            console.error(r),
                            e.status = M;
                            var n = {
                                type: "load",
                                exception: r,
                                module: e
                            };
                            e.error = n,
                            e.onError && e.onError(n),
                            d.onModuleError && d.onModuleError(n),
                            e.flush()
                        })
                    })
                }, i),
                r.js && t(r.js, function(t) {
                    L(t),
                    m(r.js, function(t) {
                        m(t.mods, function(e) {
                            if (!e.factory) {
                                var r = e.id + " is not loaded! can not find module in uri: " + t.uri;
                                console.error(r),
                                e.status = M;
                                var n = {
                                    type: "load",
                                    exception: r,
                                    module: e
                                };
                                e.error = n,
                                e.onError && e.onError(n),
                                d.onModuleError && d.onModuleError(n)
                            }
                            e.flush()
                        })
                    })
                }, i)
            },
            calculate: function(t, e, r, n, i) {
                var o, a, s, u, c, l = this;
                for (r = r || [],
                i = i || [],
                n = n || {},
                o = 0; o < t.length; o++)
                    if (s = t[o],
                    a = s.id,
                    !n[a])
                        if (c = r.length,
                        u = s.status,
                        u !== M)
                            if (d.requireModsPre && l.calculate(s.getNormalizedRequiredModules(), e, r, n, i),
                            u > x)
                                n[a] = 1;
                            else if (u === x || s.contains(l) || (u !== y && (s.status = y,
                            i.push(s)),
                            s.add(l),
                            l.wait(s)),
                            r[a])
                                console.warn("find cyclic dependency between mods: " + r),
                                n[a] = 1;
                            else {
                                r[a] = 1,
                                r.push(a),
                                d.requireModsPre || l.calculate(s.getNormalizedRequiredModules(), e, r, n, i),
                                n[a] = 1;
                                for (var f = c; f < r.length; f++)
                                    r[r[f]] = 0;
                                r.length = c
                            }
                        else
                            e.push(s),
                            n[a] = 1;
                return i
            },
            getComboMods: function(t) {
                var e, r, n, o, a, s, u, c, l, f, d, h = t.length, p = {}, m = {};
                for (e = 0; h > e; ++e)
                    if (n = t[e],
                    a = n.getType(),
                    d = n.getUri(),
                    o = n.getPackage(),
                    o ? (c = o.getBase(),
                    l = o.name,
                    u = o.getCharset(),
                    s = o.getTag(),
                    f = o.getGroup()) : c = n.id,
                    o && o.isCombine() && f) {
                        var y = p[a] || (p[a] = {});
                        f = f + "-" + u;
                        var x = y[f] || (y[f] = {})
                          , M = 0;
                        g.each(x, function(t, e) {
                            if (g.isSameOriginAs(e, c)) {
                                var r = i(e, c);
                                t.push(n),
                                s && s !== t.tag && (t.tag = v(t.tag + s)),
                                delete x[e],
                                x[r] = t,
                                M = 1
                            }
                        }),
                        M || (r = x[c] = [n],
                        r.charset = u,
                        r.tag = s || "")
                    } else {
                        var b = m[a] || (m[a] = {});
                        (r = b[c]) ? s && s !== r.tag && (r.tag = v(r.tag + s)) : (r = b[c] = [],
                        r.charset = u,
                        r.tag = s || ""),
                        r.push(n)
                    }
                return {
                    groups: p,
                    normals: m
                }
            },
            getComboUris: function(t) {
                function r(t, r, n) {
                    function a(t) {
                        if (r) {
                            if (d.useDailyAssets && t.indexOf(d.dailyAssetsHost) < 0)
                                return t.replace(d.assetsHost, d.dailyAssetsHost);
                            if (d.forceAssetsHost)
                                return t.replace(d.assetsHost, d.forceAssetsHost)
                        }
                        return t
                    }
                    function s(t) {
                        L.push({
                            combine: 1,
                            uri: a(t),
                            charset: M,
                            mods: y
                        })
                    }
                    function p() {
                        return o(m, v, r, u, c, b)
                    }
                    for (var m, v = [], y = [], x = n.tag, M = n.charset, b = x ? "?t=" + encodeURIComponent(x) + "." + t : "", E = r.length, L = [], k = 0; k < n.length; k++) {
                        var w = n[k]
                          , q = w.getUri();
                        if (w.getPackage() && w.getPackage().isCombine() && g.startsWith(q, r)) {
                            var I = q.slice(E).replace(/\?.*$/, "");
                            v.push(I),
                            y.push(w),
                            m === e ? m = -1 !== I.indexOf("/") ? I : "" : "" !== m && (m = i(m, I),
                            "/" === m && (m = "")),
                            (v.length > f || p().length > h) && (v.pop(),
                            y.pop(),
                            s(p()),
                            v = [],
                            y = [],
                            m = e,
                            k--)
                        } else
                            L.push({
                                combine: 0,
                                uri: a(q),
                                charset: M,
                                mods: [w]
                            })
                    }
                    v.length && s(p()),
                    l[t].push.apply(l[t], L)
                }
                var n, a, s, u = d.comboPrefix, c = d.comboSep, l = {}, f = d.comboMaxFileNum, h = d.comboMaxUriLength, p = this.getComboMods(t), m = p.normals, v = p.groups;
                for (n in m) {
                    l[n] = l[n] || [];
                    for (a in m[n])
                        r(n, a, m[n][a])
                }
                for (n in v) {
                    l[n] = l[n] || [];
                    for (s in v[n])
                        for (a in v[n][s])
                            r(n, a, v[n][s][a])
                }
                return l
            },
            flush: function() {
                var t = this;
                if (t.callback) {
                    for (var e = t.head, r = t.callback; e; ) {
                        var n = e.node
                          , i = n.status;
                        if (!(i >= x || i === M))
                            return;
                        n.remove(t),
                        e = t.head = e.next
                    }
                    t.callback = null,
                    r()
                }
            },
            isCompleteLoading: function() {
                return !this.head
            },
            wait: function(t) {
                var e = this;
                if (e.head) {
                    var r = {
                        node: t
                    };
                    e.tail.next = r,
                    e.tail = r
                } else
                    e.tail = e.head = {
                        node: t
                    }
            }
        }),
        f.ComboLoader = a
    };
    t.prototype.initComboLoader = a
}(feloader),
function(t) {
    var e = function() {
        var e = this.Loader
          , r = e.Utils
          , n = r.createModule
          , i = e.ComboLoader;
        r.mix(this, {
            getModule: function(t) {
                return n(t)
            },
            getPackage: function(t) {
                return this.Config.packages[t]
            },
            add: function(t, e, r) {
                i.add(t, e, r, arguments.length)
            },
            use: function(e, n, o) {
                function a(e, n) {
                    console.error("feloader: " + n + " the following modules error"),
                    console.error(r.map(e, function(t) {
                        return t.id
                    })),
                    o && (o.apply(t, e),
                    o = null)
                }
                function s() {
                    ++c;
                    var e = []
                      , i = u.calculate(h, e);
                    if (e.length)
                        a(e, "load");
                    else if (u.isCompleteLoading()) {
                        var o = r.initModules(h);
                        o ? n && (n.apply(t, r.getModulesExports(d)),
                        n = null) : a(r.collectErrors(h), "init")
                    } else
                        u.callback = s,
                        i.length && u.use(i)
                }
                var u, c = 0;
                if ("string" == typeof e && (e = e.split(/\s*,\s*/)),
                !e || e && !e.length)
                    return t;
                "object" == typeof n && (o = n.error,
                n = n.success);
                for (var l = 0; l < e.length; l++) {
                    var f = e[l];
                    (r.startsWith(f, "./") || r.startsWith(f, "../")) && (e[l] = r.normalizePath(location.href, f))
                }
                var d = r.createModules(e)
                  , h = [];
                return r.each(d, function(t) {
                    h.push.apply(h, t.getNormalizedModules())
                }),
                u = new i(s),
                s(),
                t
            },
            require: function(t) {
                return n(t).getExports()
            },
            undef: function(t) {
                var e = n(t)
                  , i = e.getNormalizedModules();
                r.each(i, function(t) {
                    t.undef()
                })
            }
        });
        var o = "??"
          , a = ",";
        this.config({
            comboPrefix: o,
            comboSep: a,
            charset: "utf-8",
            filter: "",
            lang: "zh-cn"
        }),
        this.config("packages", {
            core: {
                filter: "",
                base: "."
            }
        })
    };
    t.prototype.initLoader = e
}(feloader),
function(t) {
    var e = function() {};
    t.prototype.init = e,
    window.feloader = t = new t;
    var r = t.Env.host && t.Env.host.document
      , n = t.Loader
      , i = n.Utils
      , o = function(t) {
        return new Function("return " + t)()
    }
      , a = function(t, e) {
        var r = new RegExp("^(.*)(" + e + ")(?:-debug|)?\\.js[^/]*","i")
          , n = new RegExp("(" + e + ")(?:-debug|)?\\.js","i")
          , i = t.src || "";
        if (!i.match(n))
            return 0;
        var a = t.getAttribute("data-config");
        a = a ? o(a) : {};
        var s, u, c = a.comboPrefix, l = a.comboSep, f = i.indexOf(c);
        if (-1 === f)
            u = i.replace(r, "$1");
        else {
            u = i.substring(0, f),
            "/" !== u.charAt(u.length - 1) && (u += "/"),
            s = i.substring(f + c.length).split(l);
            for (var d = 0, h = s.length; h > d; d++) {
                var g = s[d];
                if (g.match(n)) {
                    u += g.replace(r, "$1");
                    break
                }
            }
        }
        return a.base = a.base || u,
        a
    }
      , s = function(t) {
        var e, n, i = r.getElementsByTagName("script");
        for (e = i.length - 1; e >= 0; e--)
            if (n = a(i[e], t))
                return n;
        return null
    };
    t.init = function(e) {
        var r = e.name;
        t.config(s(r))
    }
    ,
    r && r.getElementsByTagName && (t.config(i.mix({
        comboMaxUriLength: 2e3,
        comboMaxFileNum: 40
    }, s("feloader"))),
    t.config("combine", !0)),
    function() {
        function e(t) {
            var e;
            for (e = 0; e < t.length; e += 1)
                t[e](l)
        }
        function r() {
            var t = f;
            c && t.length && (f = [],
            e(t))
        }
        function n() {
            c || (c = !0,
            s && clearInterval(s),
            r())
        }
        function i(t) {
            return c ? t(l) : f.push(t),
            i
        }
        var o, a, s, u = "undefined" != typeof window && window.document, c = !u, l = u ? document : null, f = [];
        if (u) {
            if (document.addEventListener)
                document.addEventListener("DOMContentLoaded", n, !1),
                window.addEventListener("load", n, !1);
            else if (window.attachEvent) {
                window.attachEvent("onload", n),
                a = document.createElement("div");
                try {
                    o = null === window.frameElement
                } catch (d) {}
                a.doScroll && o && window.external && (s = setInterval(function() {
                    try {
                        a.doScroll(),
                        n()
                    } catch (t) {}
                }, 30))
            }
            "complete" === document.readyState && n()
        }
        i.load = function(t, e, r, n) {
            n.isBuild ? r(null) : i(r)
        }
        ,
        t.ready = i
    }();
    var u = window
      , c = u.require;
    u.require = function() {
        t.use.apply(t, arguments)
    }
    ,
    u.require.config = function() {
        t.config.apply(t, arguments)
    }
    ;
    var l = u.define;
    u.define = function() {
        t.add.apply(t, arguments)
    }
    ,
    u.define.amd = {},
    u.KISSY || (u.KISSY = t),
    t.noConflict = function() {
        u.require = c,
        u.define = l
    }
    ,
    i.ie < 10 && t.config({
        modules: {
            "@ali/mui-zepto/event": {
                alias: "@ali/mui-jquery/jquery"
            },
            "@ali/mui-zepto/form": {
                alias: "@ali/mui-jquery/jquery"
            },
            "@ali/mui-zepto/fx": {
                alias: "@ali/mui-jquery/jquery"
            },
            "@ali/mui-zepto/fx_methods": {
                alias: "@ali/mui-jquery/jquery"
            },
            "@ali/mui-zepto/gesture": {
                alias: "@ali/mui-jquery/jquery"
            },
            "@ali/mui-zepto/ie": {
                alias: "@ali/mui-jquery/jquery"
            },
            "@ali/mui-zepto/selector": {
                alias: "@ali/mui-jquery/jquery"
            },
            "@ali/mui-zepto/stack": {
                alias: "@ali/mui-jquery/jquery"
            },
            "@ali/mui-zepto/touch": {
                alias: "@ali/mui-jquery/jquery"
            },
            "@ali/mui-zepto/zepto": {
                alias: "@ali/mui-jquery/jquery"
            }
        }
    })
}(feloader);
!function(e, t) {
    "object" == typeof exports && "object" == typeof module ? module.exports = t() : "function" == typeof define && define.amd ? define([], t) : "object" == typeof exports ? exports.wpkReporter = t() : e.wpkReporter = t()
}(this, (function() {
    return function(e) {
        var t = {};
        function n(r) {
            if (t[r])
                return t[r].exports;
            var o = t[r] = {
                i: r,
                l: !1,
                exports: {}
            };
            return e[r].call(o.exports, o, o.exports, n),
            o.l = !0,
            o.exports
        }
        return n.m = e,
        n.c = t,
        n.d = function(e, t, r) {
            n.o(e, t) || Object.defineProperty(e, t, {
                enumerable: !0,
                get: r
            })
        }
        ,
        n.r = function(e) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                value: "Module"
            }),
            Object.defineProperty(e, "__esModule", {
                value: !0
            })
        }
        ,
        n.t = function(e, t) {
            if (1 & t && (e = n(e)),
            8 & t)
                return e;
            if (4 & t && "object" == typeof e && e && e.__esModule)
                return e;
            var r = Object.create(null);
            if (n.r(r),
            Object.defineProperty(r, "default", {
                enumerable: !0,
                value: e
            }),
            2 & t && "string" != typeof e)
                for (var o in e)
                    n.d(r, o, function(t) {
                        return e[t]
                    }
                    .bind(null, o));
            return r
        }
        ,
        n.n = function(e) {
            var t = e && e.__esModule ? function() {
                return e.default
            }
            : function() {
                return e
            }
            ;
            return n.d(t, "a", t),
            t
        }
        ,
        n.o = function(e, t) {
            return Object.prototype.hasOwnProperty.call(e, t)
        }
        ,
        n.p = "",
        n(n.s = 3)
    }([function(e, t) {
        e.exports = {
            sdk: {
                BID: "wpkreporter",
                CID: "jssdk",
                WID_KEY: "__wpkreporterwid_"
            },
            env: {
                BROWSER: "browser",
                NODEJS: "nodejs",
                WEEX: "weex"
            },
            px: {
                signKey: "Uvn#08uefVdwe&c4",
                addr: {
                    cn: "http://px.effirst.com/api/v1/jssdk/upload",
                    cn_https: "https://px.effirst.com/api/v1/jssdk/upload",
                    intl: "http://px-intl.ucweb.com/api/v1/jssdk/upload",
                    intl_https: "https://px-intl.ucweb.com/api/v1/jssdk/upload"
                },
                confAddr: {
                    cn: "http://px.effirst.com/api/v1/jconfig",
                    cn_https: "https://px.effirst.com/api/v1/jconfig",
                    intl: "http://px-intl.ucweb.com/api/v1/jconfig",
                    intl_https: "https://px-intl.ucweb.com/api/v1/jconfig"
                }
            },
            http: {
                methods: {
                    GET: "GET",
                    PUT: "PUT",
                    POST: "POST",
                    HEAD: "HEAD",
                    DELETE: "DELETE",
                    OPTIONS: "OPTIONS",
                    CONNECT: "OPTIONS",
                    TRACE: "OPTIONS",
                    PATCH: "OPTIONS"
                },
                protocols: {
                    HTTP: "http:",
                    HTTPS: "https:"
                }
            },
            category: {
                JSERR: 1,
                API: 2,
                JSFSPERF: 3,
                RESLOADFAIL: 4,
                FLOW: 5,
                BKPG: 6,
                HARLOG: 7
            },
            navConn: {
                types: {
                    BLUETOOTH: "bluetooth",
                    CELLULAR: "cellular",
                    ETHERNET: "ethernet",
                    MIXED: "mixed",
                    NONE: "none",
                    OTHER: "other",
                    UNKNOWN: "unknown",
                    WIFI: "wifi",
                    WIMAX: "wimax"
                },
                effectiveTypes: {
                    "2G": "2g",
                    "3G": "3g",
                    "4G": "4g",
                    SLOW2G: "slow-2g"
                }
            }
        }
    }
    , function(e, t, n) {
        var r = n(6)
          , o = n(0)
          , i = o.px
          , a = o.category;
        function s(e) {
            if (!(this instanceof s))
                return new s(e);
            e = e || {},
            this._init = !1,
            this.toolKit = r(e),
            this.logger = this.toolKit.logger,
            this.debug = e.debug || !1,
            !0 === e.debug && this.logger.warn("[wpk] now in debug mode, you can see log details"),
            this._plugins = e.plugins || [],
            this.bid = e.bid,
            this.cid = e.cid,
            this.uid = e.uid,
            this.rel = e.rel,
            this.spa = e.spa || !1,
            this.delay = !1 !== e.delay,
            this.cluster = e.cluster || "cn",
            this.sampleRate = e.sampleRate,
            this.ignoreScriptError = !1 !== e.ignoreScriptError,
            this.onlyCustom = e.onlyCustomInUCCore || e.onlyCustom || !1,
            this.ignoreU4HA = !0 === e.ignoreU4HA,
            this.beforeSend = e.beforeSend || null,
            this.checkHidden = !1 !== e.checkHidden,
            this.supportBeaconBody = !1 !== e.supportBeaconBody,
            this.blockAlipayMiniAppWebview = e.blockAlipayMiniAppWebview || !1,
            this.maxSessDuration = e.maxSessDuration || 288e5,
            this._waitingQueue = []
        }
        function c(e) {
            if (e.toolKit.inAlipayMiniAppWebview() && !0 === e.blockAlipayMiniAppWebview)
                e.logger.warn("current runtime is alipay miniapp webview, this request will be blocked.");
            else {
                var t = i.confAddr[e.cluster + (e.isHttps ? "_https" : "")]
                  , n = i.signKey;
                e._startTime = Date.now(),
                e._dying = !0,
                e.toolKit.dynamicConf(e.bid, e.VERSION, t, n, (function(t) {
                    e._dying = !1,
                    e._dyConf = t,
                    e.logger.warn("jconfig come back")
                }
                ))
            }
        }
        s.prototype = {
            VERSION: "0.9.5",
            initialize: function(e) {
                this.env = e.env,
                e.root.location && -1 !== e.root.location.search.indexOf("wpkReporterDebug=true") && (this.debug = !0),
                this.send = e.send,
                this.getWid = e.getWid,
                this.isHttps = e.isHttps,
                e.bindUnloadEvent(this)
            },
            ready: function() {
                return this._init
            },
            setConfig: function(e) {
                return this.toolKit.isObject(e) && this.toolKit.extend(this, e),
                this
            },
            report: function(e) {
                "string" == typeof e && (e = {
                    category: a.JSERR,
                    msg: e
                });
                var t = e.sampleRate || this.sampleRate;
                if (t || 0 === t || (t = 1),
                this.toolKit.canReport(t)) {
                    if (this._cleanData(e),
                    this.ready()) {
                        var n;
                        if ("function" == typeof this.beforeSend) {
                            try {
                                n = this.beforeSend(e)
                            } catch (e) {
                                this.logger.error("exec beforeSend failed for:", e)
                            }
                            if (!1 === n)
                                return void this.logger.warn("beforeSend func return false");
                            "object" == typeof n && (e = n)
                        }
                        var r = this.toolKit.getMetas()
                          , o = e.bid || this.bid || r.wpkBid
                          , s = e.cid || this.cid || r.wpkCid
                          , l = e.rel || this.rel || r.wpkRel;
                        this.toolKit.isFunction(l) && (l = l());
                        var u = e.uid || this.uid;
                        if (this.toolKit.isFunction(u) && (u = u()),
                        u || (u = this.getWid()),
                        Date.now() - this._begin >= this.maxSessDuration && (this._begin = Date.now(),
                        this._sid = this.toolKit.uuid()),
                        this.toolKit.extend(e, {
                            w_bid: o,
                            w_cid: s,
                            w_rel: l,
                            w_spa: this.spa,
                            w_tm: this.toolKit.timestamp(),
                            w_cnt: 1,
                            uid: u,
                            type: this.toolKit.categoryToType(e.category),
                            sdk_ver: this.VERSION,
                            log_src: "jssdk",
                            uc_param: this.uc_param || "",
                            wid: this.wid
                        }),
                        this._dyConf && Date.now() < this._dyConf.expireAt) {
                            var p = void 0 !== this._dyConf[e.type + "@" + e.category] ? this._dyConf[e.type + "@" + e.category] : this._dyConf[e.type];
                            if (void 0 !== (p = void 0 !== p ? p : this._dyConf.all) && !this.toolKit.canReport(p))
                                return void this.logger.warn("鐢变簬銆屽姩鎬侀厤缃€嶉噰鏍风巼鎺у埗锛屾湰鏉℃棩蹇楁渶缁堟湭涓婃姤锛岀被鍨�: ", e.type, e.category, " 閲囨牱鐜�: ", p)
                        } else
                            !this._dying && Date.now() - this._startTime >= 18e5 && (this.logger.warn("syncing dynamic config"),
                            c(this));
                        var f = {
                            app: o,
                            cp: "none",
                            de: 4,
                            seq: this.toolKit.generateSeq(),
                            tm: this.toolKit.timestamp(!0),
                            ud: encodeURIComponent(e.uid),
                            ver: e.w_rel,
                            type: e.type,
                            sver: e.sdk_ver,
                            sign: "9bf8a190ef82c5049df7b199c599c45b"
                        }
                          , d = i.addr[this.cluster + (this.isHttps ? "_https" : "")]
                          , h = this.toolKit.objToQueryString(f);
                        this.toolKit.cutStr(e, ["c1", "c2", "c3", "c4", "c5"], 128),
                        this.send(d, h, e)
                    } else
                        this._waitingQueue.push(e),
                        this.logger.warn("sdk鏈畬鎴愬垵濮嬪寲锛屾暟鎹凡缂撳瓨");
                    return this
                }
                this.logger.warn("鐢变簬閲囨牱鐜囨帶鍒讹紝鏈潯鏃ュ織鏈€缁堟湭涓婃姤锛岄噰鏍风巼: ", t)
            },
            _cleanData: function(e) {
                for (var t, n = 1; n <= 10; n++)
                    t = "bl" + n,
                    e.hasOwnProperty(t) && (e["w_" + t] = e[t],
                    e[t] = void 0);
                t = null
            },
            reportFlow: function(e) {
                return e = e || {},
                this.report(this.toolKit.extend(e || {}, {
                    category: a.FLOW,
                    sampleRate: 1
                })),
                this
            },
            reportError: function(e, t) {
                return this.toolKit.isError(e) ? ((t = t || {}).category = a.JSERR,
                t.w_msg = e.toString(),
                t.stack = this.toolKit.parseErrorStack(e),
                t.w_file = e.filename || "",
                t.w_line = e.lineno || "",
                t.w_col = e.colno || "",
                this.report(t),
                this) : this.report(e, t)
            },
            reportApiError: function(e, t) {
                return e && (this.toolKit.isObject(e.queryString) && (e.queryString = this.toolKit.objToQueryString(e.queryString)),
                this.report(this.toolKit.extend(t || {}, {
                    msg: e.msg || "",
                    w_res: e.url,
                    w_method: e.method,
                    w_param: e.queryString,
                    w_body: JSON.stringify(e.body),
                    w_resp: e.response,
                    w_rc: e.status,
                    w_rt: e.spent || 0,
                    c1: e.c1,
                    c2: e.c2,
                    c3: e.c3,
                    c4: e.c4,
                    c5: e.c5
                }, {
                    category: a.API,
                    w_type: 16
                }))),
                this
            },
            reportBlankPage: function(e) {
                return (e = e || {}).hasOwnProperty("w_fp") || this.toolKit.extend(e, {
                    w_fp: 999
                }),
                this.report(this.toolKit.extend(e || {}, {
                    category: a.BKPG
                })),
                this
            },
            diagnose: function() {
                this.ready() ? this.bid ? (this.sampleRate || this.logger.warn("娌℃湁璁剧疆閲囨牱鐜囧弬鏁皊ampleRate锛屽皢浣跨敤榛樿閲囨牱鐜�"),
                this.report({
                    _diagnose: !0
                })) : this.logger.warn("缂哄皯bid鍙傛暟,璇风‘璁ゆ槸鍚﹀凡姝ｇ‘璁剧疆") : this.logger.warn("wpkReporter灏氭湭鍒濆鍖栵紝璇风‘淇濆凡璋冪敤 install 鏂规硶")
            },
            addPlugin: function(e, t) {
                return this._plugins.push([e, t]),
                "function" == typeof e && this._init && e.apply(this, [this, t]),
                this
            },
            install: function() {
                c(this);
                for (var e = n(2), t = this._plugins.length, r = !1, o = 0; o < t; o++) {
                    var i = this._plugins[o]
                      , a = i[0]
                      , s = i[1];
                    a.prototype.pluginId === e.prototype.pluginId && (r = !0),
                    a.apply(this, [this, s])
                }
                return this.wid = this.getWid(),
                this._begin = Date.now(),
                this._sid = this.toolKit.uuid(),
                this._init = !0,
                0 !== t && r || (this.toolKit.logger.info("娌℃湁璁剧疆Flow锛屽唴缃紑鍚�"),
                this.addPlugin(e)),
                this
            },
            installAll: function() {
                var e = [[n(8), {
                    resErr: !0
                }], [n(9)], [n(10)], [n(2)], [n(11), {
                    params: "prveosfrnw"
                }]]
                  , t = this._plugins.length;
                if (0 === t)
                    this._plugins = e;
                else {
                    for (var r = [], o = e.length, i = 0; i < o; i++) {
                        for (var a = e[i], s = 0; s < t; s++)
                            if (a[0].prototype.pluginId === this._plugins[s][0].prototype.pluginId) {
                                a = this._plugins[s];
                                break
                            }
                        r.push(a)
                    }
                    this._plugins = r
                }
                return this.install()
            },
            uninstall: function() {
                return this._plugins = [],
                this._init = !1,
                this
            }
        },
        e.exports = s
    }
    , function(e, t, n) {
        var r = n(0).env
          , o = function(e) {
            var t;
            return (e ? (t = e.replace(/^#\/?/, "")) && "string" == typeof t ? t.replace(/^(https?:)?\/\//, "").replace(/\?.*$/, "") : "" : "") || "[index]"
        }
          , i = function(e, t) {
            if (t = t || {},
            e.env === r.BROWSER && window)
                if (e.toolKit.extend({
                    enable: !0
                }, t).enable) {
                    e.logger.info("wpkflowPlugin宸插紑鍚�");
                    var i, a, s = function() {
                        e.reportFlow()
                    };
                    e.toolKit.onListen(window, "load", s, !0),
                    e.spa && (n(7)(),
                    i = function(t) {
                        o(location.hash) && (e._begin = Date.now(),
                        e._sid = e.toolKit.uuid(),
                        e.reportFlow())
                    }
                    ,
                    a = function(t) {
                        o(t.detail) && (e._begin = Date.now(),
                        e._sid = e.toolKit.uuid(),
                        e.reportFlow())
                    }
                    ,
                    e.toolKit.onListen(window, "hashchange", i),
                    e.toolKit.onListen(window, "historystatechange", a)),
                    e.toolKit.onListen(window, "beforeunload", (function() {
                        e.toolKit.offListen(window, "load"),
                        e.toolKit.offListen(window, "hashchange"),
                        e.toolKit.offListen(window, "historystatechange"),
                        s = i = a = null
                    }
                    ))
                } else
                    e.logger.info("wpkflowPlugin宸插叧闂�")
        };
        i.prototype.pluginId = "flow",
        e.exports = i
    }
    , function(e, t, n) {
        (function(t) {
            var r = "object" == typeof t && t + "" == "[object process]"
              , o = "function" == typeof callNative || "function" == typeof nativeLog;
            e.exports = n(o ? 5 : r ? 13 : 16)
        }
        ).call(this, n(4))
    }
    , function(e, t) {
        var n, r, o = e.exports = {};
        function i() {
            throw new Error("setTimeout has not been defined")
        }
        function a() {
            throw new Error("clearTimeout has not been defined")
        }
        function s(e) {
            if (n === setTimeout)
                return setTimeout(e, 0);
            if ((n === i || !n) && setTimeout)
                return n = setTimeout,
                setTimeout(e, 0);
            try {
                return n(e, 0)
            } catch (t) {
                try {
                    return n.call(null, e, 0)
                } catch (t) {
                    return n.call(this, e, 0)
                }
            }
        }
        !function() {
            try {
                n = "function" == typeof setTimeout ? setTimeout : i
            } catch (e) {
                n = i
            }
            try {
                r = "function" == typeof clearTimeout ? clearTimeout : a
            } catch (e) {
                r = a
            }
        }();
        var c, l = [], u = !1, p = -1;
        function f() {
            u && c && (u = !1,
            c.length ? l = c.concat(l) : p = -1,
            l.length && d())
        }
        function d() {
            if (!u) {
                var e = s(f);
                u = !0;
                for (var t = l.length; t; ) {
                    for (c = l,
                    l = []; ++p < t; )
                        c && c[p].run();
                    p = -1,
                    t = l.length
                }
                c = null,
                u = !1,
                function(e) {
                    if (r === clearTimeout)
                        return clearTimeout(e);
                    if ((r === a || !r) && clearTimeout)
                        return r = clearTimeout,
                        clearTimeout(e);
                    try {
                        r(e)
                    } catch (t) {
                        try {
                            return r.call(null, e)
                        } catch (t) {
                            return r.call(this, e)
                        }
                    }
                }(e)
            }
        }
        function h(e, t) {
            this.fun = e,
            this.array = t
        }
        function g() {}
        o.nextTick = function(e) {
            var t = new Array(arguments.length - 1);
            if (arguments.length > 1)
                for (var n = 1; n < arguments.length; n++)
                    t[n - 1] = arguments[n];
            l.push(new h(e,t)),
            1 !== l.length || u || s(d)
        }
        ,
        h.prototype.run = function() {
            this.fun.apply(null, this.array)
        }
        ,
        o.title = "browser",
        o.browser = !0,
        o.env = {},
        o.argv = [],
        o.version = "",
        o.versions = {},
        o.on = g,
        o.addListener = g,
        o.once = g,
        o.off = g,
        o.removeListener = g,
        o.removeAllListeners = g,
        o.emit = g,
        o.prependListener = g,
        o.prependOnceListener = g,
        o.listeners = function(e) {
            return []
        }
        ,
        o.binding = function(e) {
            throw new Error("process.binding is not supported")
        }
        ,
        o.cwd = function() {
            return "/"
        }
        ,
        o.chdir = function(e) {
            throw new Error("process.chdir is not supported")
        }
        ,
        o.umask = function() {
            return 0
        }
    }
    , function(e, t, n) {
        var r = n(1)
          , o = n(12);
        e.exports = function(e) {
            var t = new r(e);
            return t.initialize(o),
            t
        }
    }
    , function(e, t) {
        var n = function(e) {
            return e || ""
        }
          , r = function() {
            var e = Date.now();
            return "undefined" != typeof window && window.performance && "function" == typeof window.performance.now && (e += performance.now()),
            "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (function(t) {
                var n = (e + 16 * Math.random()) % 16 | 0;
                return e = Math.floor(e / 16),
                ("x" === t ? n : 11 & n).toString(16)
            }
            ))
        }
          , o = function(e) {
            return "object" == typeof e
        }
          , i = function(e) {
            var t = {}.toString.call(e);
            return o(e) && ("[object Error]" === t || "[object Exception]" === t || t instanceof Error)
        }
          , a = function(e) {
            return "[object Array]" === {}.toString.call(e)
        }
          , s = function(e) {
            return "function" == typeof e
        }
          , c = function(e) {
            return "string" == typeof e
        }
          , l = function(e) {
            var t = +new Date;
            return !0 === e && (t = Math.floor(t / 1e3)),
            t
        }
          , u = function(e) {
            if (e.stack) {
                var t = e.stack.split("\n");
                return t.shift(),
                t.join("\n")
            }
            return ""
        }
          , p = function(e) {
            var t;
            switch (e) {
            case 1:
                t = "jserr";
                break;
            case 2:
                t = "api";
                break;
            case 3:
                t = "jsfsperf";
                break;
            case 4:
                t = "resloadfail";
                break;
            case 5:
                t = "flow";
                break;
            case 6:
                t = "bkpg";
                break;
            case 7:
                t = "harlog";
                break;
            default:
                t = "jssdkidx"
            }
            return t
        }
          , f = function() {
            return l() + Math.floor(10 * Math.random())
        }
          , d = function(e) {
            var t = [];
            for (var n in e)
                t.push(n + "=" + e[n]);
            return t.join("&")
        }
          , h = function(e) {
            return JSON ? JSON.stringify(e) : e.toString()
        }
          , g = function() {
            if ("undefined" != typeof document && document.getElementsByTagName)
                for (var e, t, n, r, o = document.getElementsByTagName("meta"), i = o.length, a = 0; a < i; a++)
                    "wpk-bid" === (r = o[a]).name ? e = r.content : "wpk-cid" === r.name ? t = r.content : "wpk-rel" === r.name && (n = r.content);
            return {
                wpkBid: e || null,
                wpkCid: t || null,
                wpkRel: n || null
            }
        }
          , w = function(e, t, n, r) {
            return e.addEventListener ? e.addEventListener(t, (function o(i) {
                r && e.removeEventListener(t, o, !1),
                n.call(this, i)
            }
            ), !1) : e.attachEvent && e.attachEvent("on" + t, (function o(i) {
                r && e.detachEvent("on" + t, o),
                n.call(this, i)
            }
            )),
            this
        }
          , v = function(e, t, n) {
            return n ? (e.removeEventListener ? e.removeEventListener(t, n) : e.detachEvent && e.detachEvent(t, n),
            this) : this
        }
          , y = function(e) {
            return !!e && (0 !== e && (e >= 1 || "100%" === e || (/^\d+(\.\d+)?%$/.test(e) ? Math.random() < parseFloat(e) / 100 : e > 0 && e < 1 && Math.random() < e)))
        }
          , _ = "wpk-reporter"
          , m = function(e, t) {
            var n = [].slice.call(t);
            e.apply(this, [_].concat(n))
        }
          , b = function(e) {
            var t = "";
            switch (e.category) {
            case 1:
                t = [e.category, e.uid, e.w_url, e.w_ref, e.w_msg || "", e.w_line || "", e.w_col || ""].join("");
                break;
            case 2:
                t = [e.category, e.uid, e.w_res, e.w_method, e.w_rc].join("");
                break;
            case 4:
                t = [e.category, e.uid, e.w_url, e.w_ref, e.w_res, e.w_type].join("")
            }
            return t
        }
          , x = function(e, t) {
            e = e || !1;
            try {
                if ("undefined" != typeof window && window.ucweb && window.ucweb.window || t) {
                    for (var n = (t || navigator.userAgent).split(" "), r = n.length, o = !1, i = !1, a = 0; a < r; a++)
                        if (-1 !== n[a].indexOf("UWS/")) {
                            var s = n[a].split("/");
                            i = E(s[1], "2.13.2.37")
                        } else
                            -1 !== n[a].indexOf("AliApp(DingTalk/") && (o = !0);
                    return o ? i : e
                }
            } catch (e) {}
            return !1
        }
          , E = function(e, t) {
            try {
                for (var n, r, o = e.split("."), i = t.split("."), a = o.length, s = 0; s < a; s++)
                    if ((n = parseInt(o[s])) !== (r = parseInt(i[s])))
                        return n > r;
                return !0
            } catch (e) {}
            return !1
        }
          , S = {
            get: function(e) {
                if ("undefined" != typeof localStorage) {
                    var t = localStorage.getItem(e);
                    if (t) {
                        if (t = JSON.parse(t),
                        Date.now() < t.expireAt)
                            return t;
                        this.rm(e)
                    }
                }
                return null
            },
            set: function(e, t) {
                "undefined" != typeof localStorage && e && t && (t.expireAt = Date.now() + 18e5,
                localStorage.setItem(e, JSON.stringify(t)))
            },
            rm: function(e) {
                "undefined" != typeof localStorage && localStorage.removeItem(e)
            }
        }
          , R = function(e, t) {
            if (t) {
                if (1 === t.length)
                    return e === t[0];
                if (2 === t.length) {
                    var n = t[0]
                      , r = t[1];
                    return n && !r ? o(e, n) : n && r ? o(e, n) && o(r, e) : o(r, e)
                }
                return !1
            }
            return !0;
            function o(e, t) {
                var n = e.split(".")
                  , r = t.split(".");
                return !(parseInt(n[0]) < parseInt(r[0])) && (parseInt(n[0]) > parseInt(r[0]) || !(parseInt(n[1]) < parseInt(r[1])) && (parseInt(n[1]) > parseInt(r[1]) || parseInt(n[2]) >= parseInt(r[2])))
            }
        }
          , k = function(e, t, n, o, i) {
            var a = S.get("wpkreporter:dynamicConf");
            if (a)
                s(i) && i(a);
            else {
                var c = {
                    app: e,
                    tm: l(!0),
                    ud: r(),
                    sver: t,
                    sign: "c41e43c828c16c16a6eb1c9c1e68e8ce"
                }
                  , u = d(c);
                !function(e, t) {
                    if ("undefined" == typeof XMLHttpRequest)
                        t();
                    else {
                        var n = new XMLHttpRequest;
                        n.onreadystatechange = function() {
                            if (4 === n.readyState) {
                                var e;
                                if (200 === n.status && n.response)
                                    try {
                                        var r = JSON.parse(n.response);
                                        0 === r.code && (e = r.config || [])
                                    } catch (e) {}
                                t(e)
                            }
                        }
                        ;
                        try {
                            n.open("GET", e, !0),
                            n.timeout = 3e3,
                            n.send()
                        } catch (e) {}
                    }
                }(n + "?wpk-header=" + encodeURIComponent(u), (function(e) {
                    if (a = {},
                    void 0 !== e) {
                        for (var n = e.length, r = 0; r < n; r++) {
                            var o = e[r]
                              , c = o.sdkver;
                            if (R(t, c)) {
                                if (o.common && void 0 !== o.common.sampleRate && (a.all = o.common.sampleRate),
                                o.config)
                                    for (var l, u = o.config.length, p = 0; p < u; p++)
                                        if ((l = o.config[p]).type) {
                                            if (l.category_rate)
                                                for (var f in l.category_rate)
                                                    a[l.type + "@" + f] = l.category_rate[f];
                                            l.sampleRate && (a[l.type] = l.sampleRate)
                                        }
                                break
                            }
                        }
                        S.set("wpkreporter:dynamicConf", a)
                    }
                    s(i) && i(a)
                }
                ))
            }
        }
          , O = function(e, t, n) {
            for (var r, o = t.length, i = 0; i < o; i++)
                "string" == typeof (r = e[t[i]]) ? e[t[i]] = r.substring(0, n) : "object" == typeof r && (e[t[i]] = String(r))
        }
          , T = function() {
            var e = !1;
            try {
                if ("undefined" != typeof navigator) {
                    var t = -1 !== navigator.userAgent.indexOf("Alipay")
                      , n = -1 !== navigator.userAgent.indexOf("MiniProgram")
                      , r = -1 !== navigator.userAgent.indexOf("APXWebView");
                    e = t && (n || r)
                }
            } catch (e) {}
            return e
        };
        e.exports = function(e) {
            return {
                noop: n,
                uuid: r,
                isError: i,
                isArray: a,
                isObject: o,
                isFunction: s,
                isString: c,
                logger: "undefined" != typeof console && o(console) && e.debug ? {
                    trace: function() {
                        m(console.trace, arguments)
                    },
                    debug: function() {
                        m(console.debug, arguments)
                    },
                    log: function() {
                        m(console.log, arguments)
                    },
                    info: function() {
                        m(console.info, arguments)
                    },
                    warn: function() {
                        m(console.warn, arguments)
                    },
                    error: function() {
                        m(console.error, arguments)
                    }
                } : {
                    trace: n,
                    debug: n,
                    log: n,
                    info: n,
                    warn: n,
                    error: n
                },
                extend: function(e) {
                    for (var t = 1, n = arguments.length; t < n; t++) {
                        var r = arguments[t];
                        for (var o in r)
                            Object.prototype.hasOwnProperty.call(r, o) && (e[o] = r[o])
                    }
                    return e
                },
                some: function(e, t) {
                    if (!this.isArray(e) || !this.isFunction(t))
                        return !1;
                    for (var n, r = e.length, o = 0; o < r; o++)
                        if (n = e[o],
                        t.call(this, n))
                            return !0;
                    return !1
                },
                filter: function(e, t) {
                    var n = [];
                    try {
                        for (var r = 0, o = e.length; r < o; r++)
                            t.call(this, e[r], r, e) && n.push(e[r]);
                        return n
                    } catch (e) {}
                    return e
                },
                forEach: function(e, t) {
                    if (this.isArray(e) && this.isFunction(t))
                        for (var n, r = e.length, o = 0; o < r; o++)
                            n = e[o],
                            t.call(this, n, o, e)
                },
                trim: function(e) {
                    if (this.isString(e))
                        return e.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, "")
                },
                canReport: y,
                onListen: w,
                offListen: v,
                getMetas: g,
                timestamp: l,
                generateSeq: f,
                categoryToType: p,
                parseErrorStack: u,
                objToJsonString: h,
                objToQueryString: d,
                genContentHash: b,
                isU4HA: x,
                cutStr: O,
                dynamicConf: k,
                inAlipayMiniAppWebview: T
            }
        }
    }
    , function(e, t) {
        var n = window.history || {}
          , r = window.document
          , o = function(e, t) {
            var n;
            window.CustomEvent ? n = new CustomEvent(e,{
                detail: t
            }) : ((n = r.createEvent("HTMLEvents")).initEvent(e, !1, !0),
            n.detail = t),
            window.dispatchEvent(n)
        }
          , i = function(e) {
            return e && "string" == typeof e ? e.replace(/^(https?:)?\/\//, "").replace(/\?.*$/, "") : ""
        }
          , a = function(e) {
            var t = n[e];
            "function" == typeof t && (n[e] = function(e, r, a) {
                var s = location.href
                  , c = t.call(n, e, r, a);
                if (!a || "string" != typeof a)
                    return c;
                if (a === s)
                    return c;
                try {
                    var l = s.split("#")
                      , u = a.split("#")
                      , p = i(l[0])
                      , f = i(u[0])
                      , d = l[1] && l[1].replace(/^\/?(.*)/, "$1")
                      , h = u[1] && u[1].replace(/^\/?(.*)/, "$1");
                    p !== f ? o("historystatechange", f) : d !== h && o("historystatechange", h)
                } catch (e) {}
                return c
            }
            ,
            n[e].toString = e + "() { [native code] }")
        };
        e.exports = function() {
            a("pushState"),
            a("replateState")
        }
    }
    , function(e, t, n) {
        var r, o, i = n(0), a = i.env, s = i.category, c = function(e) {
            return "function" == typeof e
        }, l = function(e) {
            var t = -1;
            switch (e.tagName.toLowerCase()) {
            case "img":
                t = 1;
                break;
            case "link":
                e.rel && "stylesheet" === e.rel.toLowerCase() && (t = 2);
                break;
            case "script":
                t = 3;
                break;
            case "video":
                t = 11
            }
            return t
        }, u = {}, p = function(e, t, n, r) {
            e.addEventListener ? e.addEventListener(t, n, r || !1) : (u["on" + t] = function() {
                return n.call(e, window.event)
            }
            ,
            e.attachEvent("on" + t, u["on" + t]))
        }, f = function(e, t) {
            var n = e.id ? "#" + e.id : ""
              , r = "";
            e.className && "string" == typeof e.className && (r = "." + e.className.split(" ").join("."));
            var o = e.tagName.toLowerCase();
            return e.parentNode && e.parentNode.tagName && t - 1 != 0 ? f(e.parentNode, t - 1) + " > " + o.toLowerCase() + n + r : o + n + r
        }, d = function(e, t, n, i, a, l) {
            if (r)
                try {
                    r.call(this, t, n, i, a, l)
                } catch (l) {}
            if ("script error" === (t || "").toLowerCase() && (t = "Script error"),
            o.ignoreScriptError && "Script error" === t)
                e.logger.warn("閰嶇疆浜唅gnoreScriptError锛屾湰娆″紓甯稿皢涓嶄笂鎶�");
            else if (!c(o.jsErrFilter) || o.jsErrFilter.call(this, event)) {
                if (null != l) {
                    var u = (l.stack || "").split("\n");
                    u.shift();
                    var p = {
                        w_msg: t,
                        w_file: n || "",
                        w_line: i || "",
                        w_col: a || "",
                        stack: u.join("\n"),
                        category: s.JSERR,
                        sampleRate: o.jsErrSampleRate
                    };
                    e.report(p)
                }
            } else
                e.logger.warn("jserrFilter 杩斿洖false锛屾湰娆℃棩蹇楀皢涓嶄笂鎶�, event: ", event)
        }, h = function(e, t) {
            var n = window;
            n && e.env === a.BROWSER ? (e.logger.info("wpkglobalerrorPlugin宸插紑鍚�"),
            !1 !== (o = e.toolKit.extend({
                jsErrSampleRate: 1,
                resErrSampleRate: 1
            }, t)).jsErr ? (r = n.onerror,
            n.onerror = function(t, n, r, o, i) {
                d(e, t, n, r, o, i)
            }
            ,
            p(n, "unhandledrejection", (function(t) {
                var n = t.type;
                "string" == typeof t.reason ? n = t.reason : t.reason && "object" == typeof t.reason && t.reason.message && (n = t.reason.message),
                d(e, n, null, null, null, t.reason || t.type)
            }
            ))) : e.logger.warn("js寮傚父鐩戞帶宸插叧闂�"),
            o.resErr ? p(n, "error", (function(t) {
                !function(e, t) {
                    if (!t.target.tagName || t.message || t.filename || t.lineno || t.colno)
                        e.logger.warn("闈炶祫婧愯幏鍙栭棶棰橈紝璺冲嚭澶勭悊, event: ", t);
                    else if (!c(o.resErrFilter) || o.resErrFilter.call(this, t)) {
                        var n = t.target.src || t.target.href;
                        e.report({
                            category: s.RESLOADFAIL,
                            sampleRate: o.resErrSampleRate,
                            msg: n + " 鍔犺浇澶辫触",
                            w_res: n,
                            w_type: l(t.target),
                            w_xpath: f(t.target, 5)
                        })
                    } else
                        e.logger.warn("reserrFilter 杩斿洖false锛屾湰娆℃棩蹇楀皢涓嶄笂鎶�, event: ", t)
                }(e, t)
            }
            ), !0) : e.logger.warn("璧勬簮鍔犺浇寮傚父鐩戞帶宸插叧闂�")) : e.logger.warn("鍏ㄥ眬閿欒鐩戞帶鎻掍欢涓嶆敮鎸侀潪娴忚鍣ㄧ幆澧�")
        };
        h.prototype.pluginId = "gerror",
        e.exports = h
    }
    , function(e, t, n) {
        var r = n(0)
          , o = r.sdk
          , i = r.http.methods
          , a = r.category
          , s = function(e) {
            return e >= 200 && e <= 299
        }
          , c = function(e) {
            return -1 === e.indexOf("//arms-retcode") && -1 === e.indexOf("//retcode.taobao.com") && -1 === e.indexOf("//retcode-sg-lazada.arms.aliyuncs.com") && -1 === e.indexOf("//mdap.alipay.com/loggw") && -1 === e.indexOf("//wpk-gateway") && -1 === e.indexOf("//px.ucweb.com") && -1 === e.indexOf("//px.effirst.com") && -1 === e.indexOf("//px-intl.ucweb.com")
        }
          , l = function(e, t) {
            if (e.hasOwnProperty(t))
                return e[t]
        }
          , u = function(e, t, n) {
            e.toolKit.isObject(n) && e.toolKit.extend(t, {
                c1: l(n, "c1"),
                c2: l(n, "c2"),
                c3: l(n, "c3"),
                c4: l(n, "c4"),
                c5: l(n, "c5"),
                bl1: l(n, "bl1"),
                bl2: l(n, "bl2"),
                bl3: l(n, "bl3"),
                bl4: l(n, "bl4"),
                bl5: l(n, "bl5")
            }),
            e.report(t)
        };
        function p(e, t) {
            var n = null;
            try {
                var r, o, i, a = e.toolKit.trim(t || "").split(/[\r\n]+/);
                if (a.length > 0)
                    n = {},
                    e.toolKit.forEach(a, (function(e) {
                        r = e.split(": "),
                        o = r.shift(),
                        i = r.join(": "),
                        n[o] = i
                    }
                    ))
            } catch (e) {}
            return n
        }
        function f(e) {
            try {
                if (!e)
                    return {};
                var t = {};
                for (var n of e)
                    t[n[0]] = n[1];
                return t
            } catch (e) {
                return {}
            }
        }
        var d = function(e, t) {
            if (e.env === r.env.BROWSER && window) {
                var n = e.toolKit.extend({
                    enable: !0,
                    sampleRate: 1
                }, t);
                n.enable ? (e.logger.info("wpkinterfacePlugin宸插紑鍚�"),
                "XMLHttpRequest"in window && function(e, t) {
                    var n = window.XMLHttpRequest.prototype
                      , r = n.open;
                    n.open = function(e, t) {
                        this.__reqCtx__ = {
                            method: e,
                            url: t || "",
                            start: Date.now()
                        };
                        var n = [].slice.call(arguments);
                        r.apply(this, n)
                    }
                    ;
                    var l = n.setRequestHeader;
                    n.setRequestHeader = function(e, t) {
                        var n = [].slice.call(arguments);
                        l.apply(this, n),
                        this.__reqCtx__ && (this.__reqCtx__.headers || (this.__reqCtx__.headers = {}),
                        this.__reqCtx__.headers[e] = t)
                    }
                    ;
                    var f = n.send;
                    n.send = function(n) {
                        var r = this;
                        function l() {
                            if (r.__reqCtx__ && 4 === r.readyState)
                                try {
                                    var l = Date.now()
                                      , f = (r.responseURL || r.__reqCtx__.url).split("?")
                                      , d = f[0]
                                      , h = f[1] || ""
                                      , g = ""
                                      , w = r.__reqCtx__.headers || {};
                                    r.__reqCtx__.method.toUpperCase() !== i.GET && n && (g = JSON.stringify(n));
                                    var v = p(e, r.getAllResponseHeaders())
                                      , y = String(r.response)
                                      , _ = !0
                                      , m = {};
                                    "function" == typeof t.errorFilter && (_ = !!(m = t.errorFilter.call(this, {
                                        url: d,
                                        status: r.status,
                                        response: y,
                                        body: g,
                                        queryString: h,
                                        reqHeaders: w,
                                        resHeaders: v
                                    })),
                                    e.logger.warn("api errorFilter鎵ц缁撴灉锛�", m)),
                                    y.length > 2048 && (y = "[response content too large]");
                                    var b = l - r.__reqCtx__.start;
                                    if (_ && b < 121e3 && c(d)) {
                                        var x = m.bizCode || r.status
                                          , E = {
                                            category: a.API,
                                            sampleRate: t.sampleRate,
                                            w_res: d,
                                            w_param: h,
                                            w_body: s(x) || !t.withBody ? "" : g,
                                            w_method: r.__reqCtx__.method,
                                            w_rc: x,
                                            w_rt: b,
                                            w_resp: s(x) || !t.withResp ? "" : m.resp || y,
                                            msg: m.msg || "",
                                            w_type: 16
                                        };
                                        u(e, E, m)
                                    }
                                } catch (t) {
                                    e.reportError(t, {
                                        bid: o.BID,
                                        cid: o.CID,
                                        category: a.JSERR,
                                        sampleRate: 1
                                    })
                                }
                        }
                        if ("onreadystatechange"in r && "function" == typeof r.onreadystatechange) {
                            var d = r.onreadystatechange;
                            r.onreadystatechange = function() {
                                var e = [].slice.call(arguments);
                                l.apply(this, e),
                                d.apply(this, e)
                            }
                        } else
                            r.onreadystatechange = l;
                        var h = [].slice.call(arguments);
                        return f.apply(this, h)
                    }
                }(e, n),
                "fetch"in window && function(e, t) {
                    var n = window.fetch;
                    window.fetch = function() {
                        var r = [].slice.call(arguments)
                          , l = i.GET;
                        r[1] && r[1].method && (l = r[1].method.toUpperCase());
                        var p = Date.now();
                        return n.apply(this, r).then((function(n) {
                            try {
                                var d = Date.now()
                                  , h = (n.url || r[0]).split("?")
                                  , g = h[0]
                                  , w = h[1] || ""
                                  , v = ""
                                  , y = null;
                                r[1] && (y = r[1].headers),
                                l !== i.GET && r[1] && r[1].body && (v = JSON.stringify(r[1].body));
                                var _ = n.clone()
                                  , m = f(_.headers);
                                _.text().then((function(r) {
                                    r = r || "";
                                    var o = !0
                                      , i = {};
                                    if ("function" == typeof t.errorFilter && (o = !!(i = t.errorFilter.call(this, {
                                        url: g,
                                        status: n.status,
                                        response: r,
                                        body: v,
                                        queryString: w,
                                        reqHeaders: y,
                                        resHeaders: m
                                    })),
                                    e.logger.warn("api errorFilter鎵ц缁撴灉锛�", i)),
                                    r = r.length > 2048 ? "[response content too large]" : r,
                                    o && d - p < 121e3 && c(g)) {
                                        var f = i.bizCode || n.status
                                          , h = {
                                            category: a.API,
                                            sampleRate: t.sampleRate,
                                            w_res: g,
                                            w_param: w,
                                            w_body: s(f) || !t.withBody ? "" : v,
                                            w_method: l,
                                            w_rc: f,
                                            w_rt: d - p,
                                            w_resp: s(f) || !t.withResp ? "" : i.resp || r,
                                            msg: i.msg || "",
                                            w_type: 16
                                        };
                                        u(e, h, i)
                                    }
                                }
                                ))
                            } catch (t) {
                                e.reportError(t, {
                                    bid: o.BID,
                                    cid: o.CID,
                                    category: a.JSERR,
                                    sampleRate: 1
                                })
                            }
                            return n
                        }
                        )).catch((function(e) {
                            throw e
                        }
                        ))
                    }
                }(e, n)) : e.logger.info("wpkinterfacePlugin宸插叧闂�")
            }
        };
        d.prototype.pluginId = "api",
        e.exports = d
    }
    , function(e, t, n) {
        var r, o = n(0).env, i = n(0).category, a = ["navigationStart", "unloadEventStart", "unloadEventEnd", "redirectStart", "redirectEnd", "fetchStart", "domainLookupStart", "domainLookupEnd", "connectStart", "secureConnectionStart", "connectEnd", "requestStart", "responseStart", "responseEnd", "domLoading", "domInteractive", "domContentLoadedEventStart", "domContentLoadedEventEnd", "domComplete", "loadEventStart", "loadEventEnd", "msFirstPaint"], s = ["navigate", "reload", "back_forward"], c = function(e) {
            var t, n = e[a[5]];
            if (1 === e._ver) {
                var r;
                if (window.chrome && window.chrome.loadTimes)
                    r = 1e3 * window.chrome.loadTimes().firstPaintTime;
                else
                    r = e.msFirstPaint ? e.msFirstPaint : e[a[13]];
                if (!r)
                    return -1;
                t = r >= n ? parseFloat((r - n).toFixed(2)) : -1
            } else
                2 === e._ver && (t = e[a[13]] - n,
                t = parseFloat(t.toFixed(2)));
            return t
        }, l = function(e, t) {
            var n, r, o, i = {};
            for (var s in t)
                o = 0,
                n = e[a[t[s][0]]],
                r = e[a[t[s][1]]],
                n > 0 && r > 0 && (o = parseFloat((r - n).toFixed(2))),
                i[s] = o;
            return i
        }, u = function(e, t) {
            var n = window;
            if (r = n.performance || n.webkitPerformance || n.msPerformance || n.mozPerformance,
            e.env === o.BROWSER && r && r.timing) {
                t = t || {};
                var a = e.toolKit.extend({
                    enable: !0,
                    sampleRate: 1
                }, t);
                if (a.enable) {
                    e.logger.info("wpkperformancePlugin宸插紑鍚�");
                    var u = r.timing || {}
                      , p = 1;
                    if ("function" == typeof n.PerformanceNavigationTiming)
                        try {
                            var f = r.getEntriesByType("navigation")[0];
                            f && (u = f,
                            p = 2)
                        } catch (e) {}
                    u._ver = p,
                    function(e, t, n, r) {
                        e.addEventListener ? e.addEventListener(t, n, r || !1) : e.attachEvent("on" + t, n)
                    }(window, "load", (function() {
                        /loaded|complete/.test(document.readyState) && setTimeout((function() {
                            var t = e.toolKit.extend(function(e) {
                                return l(e, {
                                    w_unload: [1, 2],
                                    w_redirect: [3, 4],
                                    w_appcache: [5, 6],
                                    w_dns: [6, 7],
                                    w_tcp: [8, 10],
                                    w_ssl: [9, 10],
                                    w_ttfb: [11, 12],
                                    w_contentdownload: [12, 13],
                                    w_domparsing: [13, 15],
                                    w_res: [17, 19]
                                })
                            }(u), function(e) {
                                var t = l(e, {
                                    w_firstbyte: [5, 12],
                                    w_tti: [5, 15],
                                    w_domready: [5, 17],
                                    w_load: [5, 19],
                                    w_total: [5, 20]
                                });
                                return t.w_fpt = c(e),
                                t
                            }(u));
                            for (var n in t)
                                if (t[n] < 0 || t[n] > 6e4)
                                    return void e.logger.warn("鎬ц兘鏁版嵁寮傚父锛�", n, t[n]);
                            var o = e.toolKit.extend(t, function(e) {
                                var t, n = r.navigation || {}, o = -1, i = -1, a = -1;
                                return 1 === e._ver ? t = s[n.type] || "other" : 2 === e._ver && (o = e.encodedBodySize,
                                i = e.decodedBodySize,
                                a = e.transferSize,
                                t = e.type),
                                {
                                    w_enbdsize: o,
                                    w_debdsize: i,
                                    w_transize: a,
                                    w_navtype: t
                                }
                            }(u), a, {
                                category: i.JSFSPERF
                            });
                            e.report(o)
                        }
                        ))
                    }
                    ))
                } else
                    e.logger.info("wpkperformancePlugin宸插叧闂�")
            } else
                e.logger.warn("鍩虹鎬ц兘鎻掍欢浠呮敮鎸佹祻瑙堝櫒鐜")
        };
        u.prototype.pluginId = "perf",
        e.exports = u
    }
    , function(e, t, n) {
        var r = n(0).env
          , o = function(e, t) {
            if (t = t || {},
            -1 !== [r.BROWSER, r.WEEX].indexOf(e.env) && t.params && "string" == typeof t.params) {
                e.logger.info("wpkucparamPlugin宸插紑鍚�");
                for (var n = t.params, o = ["pr", "ve", "os", "fr", "nw"], i = 0; i < 5; i++) {
                    var a = o[i];
                    -1 === n.indexOf(a) && (n += a)
                }
                try {
                    ucapi.biz.ucparams({
                        params: n,
                        success: function(t) {
                            e.uc_param = t || ""
                        }
                    })
                } catch (t) {
                    e.logger.error("get uc_param_str error: ", t),
                    e.uc_param_str = n
                }
            }
        };
        o.prototype.pluginId = "ucparam",
        e.exports = o
    }
    , function(e, t, n) {
        var r = n(0)
          , o = "undefined" != typeof weex ? weex : {}
          , i = function() {
            var e = {
                wx_pf: WXEnvironment.platform,
                wx_ver: WXEnvironment.weexVersion,
                wx_app: WXEnvironment.appName,
                wx_app_ver: WXEnvironment.appVersion,
                wx_os: WXEnvironment.osName,
                wx_os_ver: WXEnvironment.osVersion,
                wx_dev_md: WXEnvironment.deviceModel,
                dsp_w: WXEnvironment.deviceWidth,
                dsp_h: WXEnvironment.deviceHeight
            };
            if (void 0 !== weex.config.uc)
                try {
                    var t = JSON.parse(weex.config.uc.ucParams);
                    e.net = t.nw,
                    e.wx_app = t.pr,
                    e.wx_app_ver = t.ve
                } catch (e) {}
            return "undefined" != typeof weex && weex.config && weex.config.bundleType && "Vue" !== weex.config.bundleType && "vue" !== weex.config.bundleType ? ("undefined" != typeof location ? e.wx_bdl_url = location.href : e.wx_bdl_url = "undefined" != typeof weex && weex.config ? weex.config.bundleUrl : "unknow",
            e.wx_bdl_type = "Rax") : (e.wx_bdl_url = weex.config.bundleUrl,
            e.wx_bdl_type = "Vue"),
            e.wx_bdl_name = function(e) {
                try {
                    var t = e.substring(e.lastIndexOf("/") + 1);
                    return -1 === t.lastIndexOf(".") ? t : t.substring(0, t.lastIndexOf("."))
                } catch (e) {
                    return ""
                }
            }(e.wx_bdl_url),
            e
        };
        e.exports = {
            env: r.env.WEEX,
            root: o,
            isHttps: !1,
            send: function(e, t, n) {
                var r = this.toolKit.extend(i(), n, {
                    w_frmid: this._sid
                });
                r.fr = r.wx_os,
                r.rom = r.wx_os_ver,
                r.brand = r.wx_dev_md,
                r.model = r.wx_dev_md,
                r.browser = r.wx_app,
                r.bver = r.wx_app_ver,
                r.w_url = r.wx_bdl_name,
                r.w_send_mode = "weexfetch";
                var o = encodeURIComponent(t)
                  , a = encodeURIComponent(this.toolKit.objToJsonString(r));
                weex.requireModule("stream").fetch({
                    url: e,
                    method: "POST",
                    headers: {
                        "wpk-header": o
                    },
                    body: a
                }, (function(e, t) {}
                ))
            },
            getWid: function() {
                return this.toolKit.uuid()
            },
            bindUnloadEvent: function() {}
        }
    }
    , function(e, t, n) {
        var r = n(1)
          , o = n(14);
        e.exports = function(e) {
            var t = new r(e);
            return t.initialize(o),
            t
        }
    }
    , function(e, t, n) {
        (function(t) {
            var r = n(0)
              , o = t;
            e.exports = {
                env: r.env.NODEJS,
                root: o,
                send: function(e, t, n) {}
            }
        }
        ).call(this, n(15))
    }
    , function(e, t) {
        var n;
        n = function() {
            return this
        }();
        try {
            n = n || new Function("return this")()
        } catch (e) {
            "object" == typeof window && (n = window)
        }
        e.exports = n
    }
    , function(e, t, n) {
        var r = n(1)
          , o = n(17);
        e.exports = function(e) {
            var t = new r(e);
            return t.initialize(o),
            t
        }
    }
    , function(e, t, n) {
        var r = n(0)
          , o = "undefined" != typeof window ? window : "undefined" != typeof self ? self : {}
          , i = o.document
          , a = o.navigator
          , s = o.location
          , c = void 0 !== o.devicePixelRatio ? o.devicePixelRatio : 1
          , l = {}
          , u = null
          , p = function(e, t, n, r, o) {
            if (void 0 === t) {
                var a, s;
                if (!l[e]) {
                    a = new RegExp(e + "=([^;]+)");
                    try {
                        s = a.exec(i.cookie)
                    } catch (e) {
                        return null
                    }
                    s && (l[e] = s[1])
                }
                return l[e]
            }
            var c = e + "=" + t;
            r && (c += "; domain=" + r),
            o && (c += "; path=" + o),
            n && (c += "; max-age=" + n);
            try {
                return i.cookie = c,
                !!i.cookie
            } catch (e) {
                return !1
            }
        }
          , f = function(e) {
            var t = window
              , n = "wpkimgreporter_" + +new Date + ".r" + Math.floor(1e3 * Math.random())
              , r = t[n] = new Image;
            r.onload = r.onerror = function() {
                t[n] = null
            }
            ,
            r.src = e
        }
          , d = function(e) {
            var t, n = e._waitingQueue;
            if (e.checkHidden && i && i.hidden)
                return e.logger.warn("褰撳墠椤甸潰涓嶅彲瑙侊紝鏃ュ織鏁版嵁灏嗕涪寮�: ", n),
                void (e._waitingQueue = []);
            null === u && (t = (navigator ? navigator.userAgent : "").toLowerCase(),
            u = t.indexOf("windvane") > -1 && /(iphone|ipad|ipod|ios)/i.test(t));
            var r = a && a.sendBeacon && o.Blob
              , s = e.supportBeaconBody && !u;
            if (r && s) {
                var c, l, p = function(e) {
                    for (var t, n, r = [], o = [], i = e.length, a = 0; a < i; a++)
                        n = e[a].category,
                        -1 === o.indexOf(n) && o.push(n);
                    t = o.length;
                    for (var s = 0; s < t; s++) {
                        n = o[s];
                        for (var c = [], l = 0; l < i; l++) {
                            var u = e[l];
                            u.category === n && c.push(u)
                        }
                        r[s] = c
                    }
                    return r
                }(n), d = p.length;
                try {
                    for (var h, g = 0; g < d; g++) {
                        h = (c = p[g])[0]._servAddr,
                        l = c.length;
                        for (var w = 0; w < l; w++)
                            c[w].w_send_mode = "sendbeacon",
                            c[w]._servAddr = void 0,
                            c[w]._hash = void 0,
                            c[w] = e.toolKit.objToJsonString(c[w]);
                        a.sendBeacon(h, encodeURIComponent(c.join("\n")))
                    }
                    e._waitingQueue = []
                } catch (e) {}
            } else {
                for (var v, y, _ = 0; _ < n.length; _++) {
                    y = (v = n[_])._servAddr,
                    v.w_send_mode = r ? "sendbeacon" : "imgsrc",
                    v._servAddr = void 0,
                    v._hash = void 0,
                    v = encodeURIComponent(e.toolKit.objToJsonString(v));
                    try {
                        r ? a.sendBeacon(y + "&data=" + v) : f(y + "&data=" + v)
                    } catch (e) {}
                }
                e._waitingQueue = []
            }
        }
          , h = null
          , g = function(e) {
            clearTimeout(h),
            h = null,
            d(e)
        }
          , w = function(e) {
            g(e)
        };
        e.exports = {
            env: r.env.BROWSER,
            root: o,
            isHttps: s.protocol === r.http.protocols.HTTPS,
            send: function(e, t, n) {
                var l = this;
                if (!l.ignoreU4HA && l.toolKit.isU4HA(l.onlyCustom) && n.category < 100)
                    l.logger.warn("鍦╱4鍐呮牳鐜锛屽睆钄介潪鑷畾涔夌殑鎵€鏈夎嚜鍔ㄦ墦鐐�");
                else if (l.toolKit.inAlipayMiniAppWebview() && !0 === l.blockAlipayMiniAppWebview)
                    l.logger.warn("current runtime is alipay miniapp webview, this request will be blocked.");
                else {
                    var u = l.toolKit.extend(function(e) {
                        if (!i)
                            return {};
                        var t, n = i.referrer;
                        return n && -1 !== n.indexOf('"') && (n = encodeURIComponent(i.referrer)),
                        {
                            w_url: s.origin + s.pathname,
                            w_query: s.search,
                            w_ref: s.hash.substring(1),
                            w_title: i.title,
                            ua: a.userAgent,
                            referrer: n,
                            dsp_dpi: c || 1,
                            dsp_w: o.screen.width,
                            dsp_h: o.screen.height,
                            net: (t = a.connection,
                            t && t.type ? t.type === r.navConn.types.NONE ? "disconnected" : t.type === r.navConn.types.CELLULAR ? t.effectiveType === r.navConn.effectiveTypes.SLOW2G ? "2g" : t.effectiveType : t.type : "")
                        }
                    }(l.spa), n, {
                        w_frmid: l._sid
                    });
                    if (l.logger.warn("logData to send: ", e, u),
                    e += "?wpk-header=" + encodeURIComponent(t),
                    l.uc_param_str && (e += "&uc_param_str=" + l.uc_param_str),
                    !0 === n._diagnose)
                        return u = encodeURIComponent(l.toolKit.objToJsonString(u)),
                        void window.open(e + "&data=" + u);
                    u._servAddr = e,
                    u._hash = l.toolKit.genContentHash(u);
                    var p, f, d = l.delay && -1 !== [1, 2, 4].indexOf(u.category);
                    if (function(e, t) {
                        var n = e._waitingQueue
                          , r = n.length
                          , o = t.reduplication || e.reduplication || !0
                          , i = !0;
                        if (1 === t.category && o && 0 !== r) {
                            for (var a, s = 0; s < r; s++)
                                if ((a = n[s])._hash === t._hash) {
                                    a.w_cnt++,
                                    i = !1;
                                    break
                                }
                            i && n.push(t)
                        } else
                            n.push(t);
                        return i
                    }(l, u) || !d)
                        p = function() {
                            g(l)
                        }
                        ,
                        h = -1 === (f = d ? 3e3 : -1) ? (p(),
                        null) : setTimeout(p, f || 0);
                    else
                        l.logger.warn("logData琚悎骞�: ", u)
                }
            },
            getWid: function() {
                var e = p(r.sdk.WID_KEY);
                return e || (e = this.toolKit.uuid(),
                p(r.sdk.WID_KEY, e, 15552e3)),
                e
            },
            bindUnloadEvent: function(e) {
                window && (window.addEventListener ? window.addEventListener("beforeunload", (function(t) {
                    w(e)
                }
                ), !1) : window.attachEvent && window.attachEvent("onbeforeunload", (function(t) {
                    w(e)
                }
                )))
            }
        }
    }
    ])
}
));
!function(e, t) {
    "object" == typeof exports && "object" == typeof module ? module.exports = t() : "function" == typeof define && define.amd ? define([], t) : "object" == typeof exports ? exports.wpkblankPlugin = t() : e.wpkblankPlugin = t()
}(this, (function() {
    return function(e) {
        var t = {};
        function n(o) {
            if (t[o])
                return t[o].exports;
            var r = t[o] = {
                i: o,
                l: !1,
                exports: {}
            };
            return e[o].call(r.exports, r, r.exports, n),
            r.l = !0,
            r.exports
        }
        return n.m = e,
        n.c = t,
        n.d = function(e, t, o) {
            n.o(e, t) || Object.defineProperty(e, t, {
                enumerable: !0,
                get: o
            })
        }
        ,
        n.r = function(e) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                value: "Module"
            }),
            Object.defineProperty(e, "__esModule", {
                value: !0
            })
        }
        ,
        n.t = function(e, t) {
            if (1 & t && (e = n(e)),
            8 & t)
                return e;
            if (4 & t && "object" == typeof e && e && e.__esModule)
                return e;
            var o = Object.create(null);
            if (n.r(o),
            Object.defineProperty(o, "default", {
                enumerable: !0,
                value: e
            }),
            2 & t && "string" != typeof e)
                for (var r in e)
                    n.d(o, r, function(t) {
                        return e[t]
                    }
                    .bind(null, r));
            return o
        }
        ,
        n.n = function(e) {
            var t = e && e.__esModule ? function() {
                return e.default
            }
            : function() {
                return e
            }
            ;
            return n.d(t, "a", t),
            t
        }
        ,
        n.o = function(e, t) {
            return Object.prototype.hasOwnProperty.call(e, t)
        }
        ,
        n.p = "",
        n(n.s = 1)
    }([function(e, t) {
        e.exports = {
            sdk: {
                BID: "wpkreporter",
                CID: "jssdk",
                WID_KEY: "__wpkreporterwid_"
            },
            env: {
                BROWSER: "browser",
                NODEJS: "nodejs",
                WEEX: "weex"
            },
            px: {
                signKey: "Uvn#08uefVdwe&c4",
                addr: {
                    cn: "http://px.effirst.com/api/v1/jssdk/upload",
                    cn_https: "https://px.effirst.com/api/v1/jssdk/upload",
                    intl: "http://px-intl.ucweb.com/api/v1/jssdk/upload",
                    intl_https: "https://px-intl.ucweb.com/api/v1/jssdk/upload"
                },
                confAddr: {
                    cn: "http://px.effirst.com/api/v1/jconfig",
                    cn_https: "https://px.effirst.com/api/v1/jconfig",
                    intl: "http://px-intl.ucweb.com/api/v1/jconfig",
                    intl_https: "https://px-intl.ucweb.com/api/v1/jconfig"
                }
            },
            http: {
                methods: {
                    GET: "GET",
                    PUT: "PUT",
                    POST: "POST",
                    HEAD: "HEAD",
                    DELETE: "DELETE",
                    OPTIONS: "OPTIONS",
                    CONNECT: "OPTIONS",
                    TRACE: "OPTIONS",
                    PATCH: "OPTIONS"
                },
                protocols: {
                    HTTP: "http:",
                    HTTPS: "https:"
                }
            },
            category: {
                JSERR: 1,
                API: 2,
                JSFSPERF: 3,
                RESLOADFAIL: 4,
                FLOW: 5,
                BKPG: 6,
                HARLOG: 7,
                PERFNEXT: 1e3
            },
            navConn: {
                types: {
                    BLUETOOTH: "bluetooth",
                    CELLULAR: "cellular",
                    ETHERNET: "ethernet",
                    MIXED: "mixed",
                    NONE: "none",
                    OTHER: "other",
                    UNKNOWN: "unknown",
                    WIFI: "wifi",
                    WIMAX: "wimax"
                },
                effectiveTypes: {
                    "2G": "2g",
                    "3G": "3g",
                    "4G": "4g",
                    SLOW2G: "slow-2g"
                }
            }
        }
    }
    , function(e, t, n) {
        var o = n(0)
          , r = function(e, t) {
            if (e.env === o.env.BROWSER && "undefined" != typeof window) {
                var n = {
                    enable: !0,
                    sampleRate: t.sampleRate || 1,
                    rootNode: t.rootNode,
                    ignorePageUrls: t.ignorePageUrls || null,
                    maxDepth: t.maxDepth || 8,
                    minElements: t.minElements || 10,
                    keyNoteText: t.keyNoteText || [],
                    onloadDuration: t.onloadDuration || 8e3,
                    wsDuration: t.wsDuration || 3e3,
                    startCheckingTime: t.startCheckingTime || 5e3
                }
                  , r = e.toolKit.extend(n, t);
                if (r.enable) {
                    e.logger.info("wpkblankPagePlugin宸插紑鍚�");
                    try {
                        if (e.toolKit.isFunction(r.ignorePageUrls) && r.ignorePageUrls(location))
                            return void e.logger.info("褰撳墠椤甸潰鍦ㄧ櫧灞忔娴嬬殑鐧藉悕鍗曚腑")
                    } catch (e) {}
                    var i = !1;
                    if (r.onloadDuration > 0)
                        var a = setTimeout(()=>{
                            i = !0,
                            e.reportBlankPage({
                                w_fp: 100,
                                w_wst: r.onloadDuration
                            }),
                            clearTimeout(a)
                        }
                        , r.onloadDuration);
                    var l = function() {
                        clearTimeout(a);
                        try {
                            !i && r.wsDuration > 0 && function(e, t) {
                                var n = performance.timing;
                                if ("function" == typeof window.PerformanceNavigationTiming)
                                    try {
                                        var o = performance.getEntriesByType("navigation")[0];
                                        o && (n = o)
                                    } catch (e) {}
                                if (n)
                                    try {
                                        n.responseEnd - n.fetchStart >= e && t()
                                    } catch (e) {}
                            }(r.wsDuration, (function() {
                                e.reportBlankPage({
                                    w_fp: 104,
                                    w_wst: r.wsDuration
                                })
                            }
                            ));
                            var t = setTimeout((function() {
                                !function(e, t) {
                                    var n, o, r, i, a = 0, l = 0, p = !1, c = [], s = function(e) {
                                        return 0 === e.style.width || 0 === e.style.height || "none" === e.style.display || 0 === e.style.opacity || "hidden" === e.style.visibility || "collapse" === e.style.visibility || void 0 !== e.type && "hidden" === e.type
                                    }, f = function(e) {
                                        return e && -1 !== ["VIDEO", "IMG", "BUTTON", "TEXTAREA", "RADIO", "CHECKBOX", "SELECT", "IFRAME", "CANVAS", "SVG"].indexOf(e.nodeName)
                                    }, u = function(n, o) {
                                        for (var r = Array.prototype.slice.call(n); r.length; ) {
                                            var i = r.shift();
                                            o > a && (a = o),
                                            c.push({
                                                tag: i.tagName,
                                                layer: o,
                                                cls: i.className
                                            });
                                            var d = s(i);
                                            if (e.logger.info("depth锛�" + o, i.nodeType, i.tagName, d),
                                            !d) {
                                                if (l++,
                                                f(i)) {
                                                    p = !0,
                                                    e.logger.info("鏈夊彲瑙佸厓绱狅紝闈炵櫧灞�");
                                                    break
                                                }
                                                o <= t.maxDepth && !s(i) && i.children.length && u(i.children, o + 1)
                                            }
                                        }
                                    }, d = t.rootNode || document.body, g = !1;
                                    if (d)
                                        if (o = d.innerText)
                                            r = t.keyNoteText,
                                            i = o,
                                            e.toolKit.some(r, (function(e) {
                                                return e === i
                                            }
                                            )) ? (g = !0,
                                            n = 102,
                                            e.logger.warn("鑲畾鐧藉睆锛屽懡涓叧閿瓧", o)) : (g = !1,
                                            p = !0);
                                        else {
                                            var y = Array.prototype.slice.call(d.children)
                                              , m = e.toolKit.filter(y, (function(e) {
                                                return -1 === ["STYLE", "SCRIPT", "LINK"].indexOf(e.nodeName)
                                            }
                                            ));
                                            u(m, 1)
                                        }
                                    else
                                        g = !0,
                                        n = 103,
                                        e.logger.warn("鐧藉睆锛屾湪鏈塨ody鏍囩鎴栬€呮寚瀹氱殑root鑺傜偣涓虹┖");
                                    e.logger.warn("鍏冪礌鏁�: ", l),
                                    e.logger.warn("閬嶅巻鐨勬渶澶у眰绾�: ", a),
                                    e.logger.warn("dsl", c),
                                    !g && !p && l < t.minElements && (g = !0,
                                    n = 101),
                                    g && (e.logger.warn("鐧藉睆浜�", n),
                                    e.reportBlankPage({
                                        w_fp: n,
                                        w_dsl: JSON.stringify(c),
                                        w_depth: a,
                                        w_domcnt: l
                                    }))
                                }(e, r),
                                clearTimeout(t)
                            }
                            ), r.startCheckingTime)
                        } catch (t) {
                            e.logger.error("bkpg checking oops: ", t)
                        }
                    };
                    e.toolKit.onListen(window, "load", l, !0),
                    e.toolKit.onListen(window, "beforeunload", (function() {
                        e.toolKit.offListen(window, "load"),
                        l = null
                    }
                    ))
                } else
                    e.logger.info("wpkblankPagePlugin宸插叧闂�")
            }
        };
        r.prototype.pluginId = "bkpg",
        e.exports = r
    }
    ])
}
));
;;var _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
    return typeof e
}
: function(e) {
    return e && "function" == typeof Symbol && e.constructor === Symbol ? "symbol" : typeof e
}
  , _classCallCheck = function(e, t) {
    if (!(e instanceof t))
        throw new TypeError("Cannot call a class as a function")
}
  , _createClass = function() {
    function e(e, t) {
        for (var r = 0; r < t.length; r++) {
            var n = t[r];
            n.enumerable = n.enumerable || !1,
            n.configurable = !0,
            "value"in n && (n.writable = !0),
            Object.defineProperty(e, n.key, n)
        }
    }
    return function(t, r, n) {
        return r && e(t.prototype, r),
        n && e(t, n),
        t
    }
}()
  , _defineProperty = function(e, t, r) {
    return t in e ? Object.defineProperty(e, t, {
        value: r,
        enumerable: !0,
        configurable: !0,
        writable: !0
    }) : e[t] = r,
    e
}
  , _extends = Object.assign || function(e) {
    for (var t = 1; t < arguments.length; t++) {
        var r = arguments[t];
        for (var n in r)
            Object.prototype.hasOwnProperty.call(r, n) && (e[n] = r[n])
    }
    return e
}
  , _inherits = function(e, t) {
    if ("function" != typeof t && null !== t)
        throw new TypeError("Super expression must either be null or a function, not " + typeof t);
    e.prototype = Object.create(t && t.prototype, {
        constructor: {
            value: e,
            enumerable: !1,
            writable: !0,
            configurable: !0
        }
    }),
    t && (Object.setPrototypeOf ? Object.setPrototypeOf(e, t) : e.__proto__ = t)
}
  , _interopRequireDefault = function(e) {
    return e && e.__esModule ? e : {
        "default": e
    }
}
  , _interopRequireWildcard = function(e) {
    if (e && e.__esModule)
        return e;
    var t = {};
    if (null != e)
        for (var r in e)
            Object.prototype.hasOwnProperty.call(e, r) && (t[r] = e[r]);
    return t["default"] = e,
    t
}
  , _possibleConstructorReturn = function(e, t) {
    if (!e)
        throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
    return !t || "object" != typeof t && "function" != typeof t ? e : t
}
  , _slicedToArray = function() {
    function e(e, t) {
        var r = []
          , n = !0
          , o = !1
          , i = void 0;
        try {
            for (var u, a = e[Symbol.iterator](); !(n = (u = a.next()).done) && (r.push(u.value),
            !t || r.length !== t); n = !0)
                ;
        } catch (f) {
            o = !0,
            i = f
        } finally {
            try {
                !n && a["return"] && a["return"]()
            } finally {
                if (o)
                    throw i
            }
        }
        return r
    }
    return function(t, r) {
        if (Array.isArray(t))
            return t;
        if (Symbol.iterator in Object(t))
            return e(t, r);
        throw new TypeError("Invalid attempt to destructure non-iterable instance")
    }
}();
var runtime = (function(G) {
    var r = Object.prototype;
    var u = r.hasOwnProperty;
    var l;
    var F = typeof Symbol === "function" ? Symbol : {};
    var C = F.iterator || "@@iterator";
    var v = F.asyncIterator || "@@asyncIterator";
    var t = F.toStringTag || "@@toStringTag";
    function e(J, H, I) {
        Object.defineProperty(J, H, {
            value: I,
            enumerable: true,
            configurable: true,
            writable: true
        });
        return J[H]
    }
    try {
        e({}, "")
    } catch (k) {
        e = function(J, H, I) {
            return J[H] = I
        }
    }
    function o(N, H, J, I) {
        var L = H && H.prototype instanceof h ? H : h;
        var M = Object.create(L.prototype);
        var K = new z(I || []);
        M._invoke = f(N, J, K);
        return M
    }
    G.wrap = o;
    function n(I, K, H) {
        try {
            return {
                type: "normal",
                arg: I.call(K, H)
            }
        } catch (J) {
            return {
                type: "throw",
                arg: J
            }
        }
    }
    var d = "suspendedStart";
    var A = "suspendedYield";
    var B = "executing";
    var i = "completed";
    var j = {};
    function h() {}
    function x() {}
    function m() {}
    var s = {};
    s[C] = function() {
        return this
    }
    ;
    var b = Object.getPrototypeOf;
    var g = b && b(b(c([])));
    if (g && g !== r && u.call(g, C)) {
        s = g
    }
    var E = m.prototype = h.prototype = Object.create(s);
    x.prototype = E.constructor = m;
    m.constructor = x;
    x.displayName = e(m, t, "GeneratorFunction");
    function D(H) {
        ["next", "throw", "return"].forEach(function(I) {
            e(H, I, function(J) {
                return this._invoke(I, J)
            })
        })
    }
    G.isGeneratorFunction = function(I) {
        var H = typeof I === "function" && I.constructor;
        return H ? H === x || (H.displayName || H.name) === "GeneratorFunction" : false
    }
    ;
    G.mark = function(H) {
        if (Object.setPrototypeOf) {
            Object.setPrototypeOf(H, m)
        } else {
            H.__proto__ = m;
            e(H, t, "GeneratorFunction")
        }
        H.prototype = Object.create(E);
        return H
    }
    ;
    G.awrap = function(H) {
        return {
            __await: H
        }
    }
    ;
    function y(K, J) {
        function I(S, N, R, Q) {
            var O = n(K[S], K, N);
            if (O.type === "throw") {
                Q(O.arg)
            } else {
                var M = O.arg;
                var P = M.value;
                if (P && typeof P === "object" && u.call(P, "__await")) {
                    return J.resolve(P.__await).then(function(T) {
                        I("next", T, R, Q)
                    }, function(T) {
                        I("throw", T, R, Q)
                    })
                }
                return J.resolve(P).then(function(T) {
                    M.value = T;
                    R(M)
                }, function(T) {
                    return I("throw", T, R, Q)
                })
            }
        }
        var L;
        function H(O, M) {
            function N() {
                return new J(function(Q, P) {
                    I(O, M, Q, P)
                }
                )
            }
            return L = L ? L.then(N, N) : N()
        }
        this._invoke = H
    }
    D(y.prototype);
    y.prototype[v] = function() {
        return this
    }
    ;
    G.AsyncIterator = y;
    G.async = function(M, H, K, J, L) {
        if (L === void 0) {
            L = Promise
        }
        var I = new y(o(M, H, K, J),L);
        return G.isGeneratorFunction(H) ? I : I.next().then(function(N) {
            return N.done ? N.value : I.next()
        })
    }
    ;
    function f(L, H, J) {
        var K = d;
        return function I(Q, M) {
            if (K === B) {
                throw new Error("Generator is already running")
            }
            if (K === i) {
                if (Q === "throw") {
                    throw M
                }
                return w()
            }
            J.method = Q;
            J.arg = M;
            while (true) {
                var O = J.delegate;
                if (O) {
                    var P = q(O, J);
                    if (P) {
                        if (P === j) {
                            continue
                        }
                        return P
                    }
                }
                if (J.method === "next") {
                    J.sent = J._sent = J.arg
                } else {
                    if (J.method === "throw") {
                        if (K === d) {
                            K = i;
                            throw J.arg
                        }
                        J.dispatchException(J.arg)
                    } else {
                        if (J.method === "return") {
                            J.abrupt("return", J.arg)
                        }
                    }
                }
                K = B;
                var N = n(L, H, J);
                if (N.type === "normal") {
                    K = J.done ? i : A;
                    if (N.arg === j) {
                        continue
                    }
                    return {
                        value: N.arg,
                        done: J.done
                    }
                } else {
                    if (N.type === "throw") {
                        K = i;
                        J.method = "throw";
                        J.arg = N.arg
                    }
                }
            }
        }
    }
    function q(J, I) {
        var L = J.iterator[I.method];
        if (L === l) {
            I.delegate = null;
            if (I.method === "throw") {
                if (J.iterator["return"]) {
                    I.method = "return";
                    I.arg = l;
                    q(J, I);
                    if (I.method === "throw") {
                        return j
                    }
                }
                I.method = "throw";
                I.arg = new TypeError("The iterator does not provide a 'throw' method")
            }
            return j
        }
        var H = n(L, J.iterator, I.arg);
        if (H.type === "throw") {
            I.method = "throw";
            I.arg = H.arg;
            I.delegate = null;
            return j
        }
        var K = H.arg;
        if (!K) {
            I.method = "throw";
            I.arg = new TypeError("iterator result is not an object");
            I.delegate = null;
            return j
        }
        if (K.done) {
            I[J.resultName] = K.value;
            I.next = J.nextLoc;
            if (I.method !== "return") {
                I.method = "next";
                I.arg = l
            }
        } else {
            return K
        }
        I.delegate = null;
        return j
    }
    D(E);
    e(E, t, "Generator");
    E[C] = function() {
        return this
    }
    ;
    E.toString = function() {
        return "[object Generator]"
    }
    ;
    function p(I) {
        var H = {
            tryLoc: I[0]
        };
        if (1 in I) {
            H.catchLoc = I[1]
        }
        if (2 in I) {
            H.finallyLoc = I[2];
            H.afterLoc = I[3]
        }
        this.tryEntries.push(H)
    }
    function a(I) {
        var H = I.completion || {};
        H.type = "normal";
        delete H.arg;
        I.completion = H
    }
    function z(H) {
        this.tryEntries = [{
            tryLoc: "root"
        }];
        H.forEach(p, this);
        this.reset(true)
    }
    G.keys = function(H) {
        var K = [];
        for (var I in H) {
            K.push(I)
        }
        K.reverse();
        return function J() {
            while (K.length) {
                var L = K.pop();
                if (L in H) {
                    J.value = L;
                    J.done = false;
                    return J
                }
            }
            J.done = true;
            return J
        }
    }
    ;
    function c(J) {
        if (J) {
            var K = J[C];
            if (K) {
                return K.call(J)
            }
            if (typeof J.next === "function") {
                return J
            }
            if (!isNaN(J.length)) {
                var H = -1
                  , I = function I() {
                    while (++H < J.length) {
                        if (u.call(J, H)) {
                            I.value = J[H];
                            I.done = false;
                            return I
                        }
                    }
                    I.value = l;
                    I.done = true;
                    return I
                };
                return I.next = I
            }
        }
        return {
            next: w
        }
    }
    G.values = c;
    function w() {
        return {
            value: l,
            done: true
        }
    }
    z.prototype = {
        constructor: z,
        reset: function(I) {
            this.prev = 0;
            this.next = 0;
            this.sent = this._sent = l;
            this.done = false;
            this.delegate = null;
            this.method = "next";
            this.arg = l;
            this.tryEntries.forEach(a);
            if (!I) {
                for (var H in this) {
                    if (H.charAt(0) === "t" && u.call(this, H) && !isNaN(+H.slice(1))) {
                        this[H] = l
                    }
                }
            }
        },
        stop: function() {
            this.done = true;
            var H = this.tryEntries[0];
            var I = H.completion;
            if (I.type === "throw") {
                throw I.arg
            }
            return this.rval
        },
        dispatchException: function(L) {
            if (this.done) {
                throw L
            }
            var K = this;
            function O(Q, P) {
                H.type = "throw";
                H.arg = L;
                K.next = Q;
                if (P) {
                    K.method = "next";
                    K.arg = l
                }
                return !!P
            }
            for (var J = this.tryEntries.length - 1; J >= 0; --J) {
                var N = this.tryEntries[J];
                var H = N.completion;
                if (N.tryLoc === "root") {
                    return O("end")
                }
                if (N.tryLoc <= this.prev) {
                    var M = u.call(N, "catchLoc");
                    var I = u.call(N, "finallyLoc");
                    if (M && I) {
                        if (this.prev < N.catchLoc) {
                            return O(N.catchLoc, true)
                        } else {
                            if (this.prev < N.finallyLoc) {
                                return O(N.finallyLoc)
                            }
                        }
                    } else {
                        if (M) {
                            if (this.prev < N.catchLoc) {
                                return O(N.catchLoc, true)
                            }
                        } else {
                            if (I) {
                                if (this.prev < N.finallyLoc) {
                                    return O(N.finallyLoc)
                                }
                            } else {
                                throw new Error("try statement without catch or finally")
                            }
                        }
                    }
                }
            }
        },
        abrupt: function(L, H) {
            for (var J = this.tryEntries.length - 1; J >= 0; --J) {
                var M = this.tryEntries[J];
                if (M.tryLoc <= this.prev && u.call(M, "finallyLoc") && this.prev < M.finallyLoc) {
                    var K = M;
                    break
                }
            }
            if (K && (L === "break" || L === "continue") && K.tryLoc <= H && H <= K.finallyLoc) {
                K = null
            }
            var I = K ? K.completion : {};
            I.type = L;
            I.arg = H;
            if (K) {
                this.method = "next";
                this.next = K.finallyLoc;
                return j
            }
            return this.complete(I)
        },
        complete: function(I, H) {
            if (I.type === "throw") {
                throw I.arg
            }
            if (I.type === "break" || I.type === "continue") {
                this.next = I.arg
            } else {
                if (I.type === "return") {
                    this.rval = this.arg = I.arg;
                    this.method = "return";
                    this.next = "end"
                } else {
                    if (I.type === "normal" && H) {
                        this.next = H
                    }
                }
            }
            return j
        },
        finish: function(H) {
            for (var I = this.tryEntries.length - 1; I >= 0; --I) {
                var J = this.tryEntries[I];
                if (J.finallyLoc === H) {
                    this.complete(J.completion, J.afterLoc);
                    a(J);
                    return j
                }
            }
        },
        "catch": function(I) {
            for (var J = this.tryEntries.length - 1; J >= 0; --J) {
                var L = this.tryEntries[J];
                if (L.tryLoc === I) {
                    var H = L.completion;
                    if (H.type === "throw") {
                        var K = H.arg;
                        a(L)
                    }
                    return K
                }
            }
            throw new Error("illegal catch attempt")
        },
        delegateYield: function(I, J, H) {
            this.delegate = {
                iterator: c(I),
                resultName: J,
                nextLoc: H
            };
            if (this.method === "next") {
                this.arg = l
            }
            return j
        }
    };
    return G
}(typeof module === "object" ? module.exports : {}));
try {
    regeneratorRuntime = runtime
} catch (accidentalStrictMode) {
    Function("r", "regeneratorRuntime = r")(runtime)
}
;!function(a, b) {
    function c() {
        var a = {}
          , b = new q(function(b, c) {
            a.resolve = b,
            a.reject = c
        }
        );
        return a.promise = b,
        a
    }
    function d(a, b) {
        for (var c in b)
            void 0 === a[c] && (a[c] = b[c]);
        return a
    }
    function e(a) {
        var b = document.getElementsByTagName("head")[0] || document.getElementsByTagName("body")[0] || document.firstElementChild || document;
        b.appendChild(a)
    }
    function f(a) {
        var b = [];
        for (var c in a)
            a[c] && b.push(c + "=" + encodeURIComponent(a[c]));
        return b.join("&")
    }
    function g(a) {
        try {
            return ".com" !== a.substring(a.lastIndexOf(".")) ? (a.split(".") || []).length <= 3 ? a : a.split(".").slice(1).join(".") : a.substring(a.lastIndexOf(".", a.lastIndexOf(".") - 1) + 1)
        } catch (b) {
            return a.substring(a.lastIndexOf(".", a.lastIndexOf(".") - 1) + 1)
        }
    }
    function h(a) {
        function b(a, b) {
            return a << b | a >>> 32 - b
        }
        function c(a, b) {
            var c, d, e, f, g;
            return e = 2147483648 & a,
            f = 2147483648 & b,
            c = 1073741824 & a,
            d = 1073741824 & b,
            g = (1073741823 & a) + (1073741823 & b),
            c & d ? 2147483648 ^ g ^ e ^ f : c | d ? 1073741824 & g ? 3221225472 ^ g ^ e ^ f : 1073741824 ^ g ^ e ^ f : g ^ e ^ f
        }
        function d(a, b, c) {
            return a & b | ~a & c
        }
        function e(a, b, c) {
            return a & c | b & ~c
        }
        function f(a, b, c) {
            return a ^ b ^ c
        }
        function g(a, b, c) {
            return b ^ (a | ~c)
        }
        function h(a, e, f, g, h, i, j) {
            return a = c(a, c(c(d(e, f, g), h), j)),
            c(b(a, i), e)
        }
        function i(a, d, f, g, h, i, j) {
            return a = c(a, c(c(e(d, f, g), h), j)),
            c(b(a, i), d)
        }
        function j(a, d, e, g, h, i, j) {
            return a = c(a, c(c(f(d, e, g), h), j)),
            c(b(a, i), d)
        }
        function k(a, d, e, f, h, i, j) {
            return a = c(a, c(c(g(d, e, f), h), j)),
            c(b(a, i), d)
        }
        function l(a) {
            for (var b, c = a.length, d = c + 8, e = (d - d % 64) / 64, f = 16 * (e + 1), g = new Array(f - 1), h = 0, i = 0; c > i; )
                b = (i - i % 4) / 4,
                h = i % 4 * 8,
                g[b] = g[b] | a.charCodeAt(i) << h,
                i++;
            return b = (i - i % 4) / 4,
            h = i % 4 * 8,
            g[b] = g[b] | 128 << h,
            g[f - 2] = c << 3,
            g[f - 1] = c >>> 29,
            g
        }
        function m(a) {
            var b, c, d = "", e = "";
            for (c = 0; 3 >= c; c++)
                b = a >>> 8 * c & 255,
                e = "0" + b.toString(16),
                d += e.substr(e.length - 2, 2);
            return d
        }
        function n(a) {
            a = a.replace(/\r\n/g, "\n");
            for (var b = "", c = 0; c < a.length; c++) {
                var d = a.charCodeAt(c);
                128 > d ? b += String.fromCharCode(d) : d > 127 && 2048 > d ? (b += String.fromCharCode(d >> 6 | 192),
                b += String.fromCharCode(63 & d | 128)) : (b += String.fromCharCode(d >> 12 | 224),
                b += String.fromCharCode(d >> 6 & 63 | 128),
                b += String.fromCharCode(63 & d | 128))
            }
            return b
        }
        var o, p, q, r, s, t, u, v, w, x = [], y = 7, z = 12, A = 17, B = 22, C = 5, D = 9, E = 14, F = 20, G = 4, H = 11, I = 16, J = 23, K = 6, L = 10, M = 15, N = 21;
        for (a = n(a),
        x = l(a),
        t = 1732584193,
        u = 4023233417,
        v = 2562383102,
        w = 271733878,
        o = 0; o < x.length; o += 16)
            p = t,
            q = u,
            r = v,
            s = w,
            t = h(t, u, v, w, x[o + 0], y, 3614090360),
            w = h(w, t, u, v, x[o + 1], z, 3905402710),
            v = h(v, w, t, u, x[o + 2], A, 606105819),
            u = h(u, v, w, t, x[o + 3], B, 3250441966),
            t = h(t, u, v, w, x[o + 4], y, 4118548399),
            w = h(w, t, u, v, x[o + 5], z, 1200080426),
            v = h(v, w, t, u, x[o + 6], A, 2821735955),
            u = h(u, v, w, t, x[o + 7], B, 4249261313),
            t = h(t, u, v, w, x[o + 8], y, 1770035416),
            w = h(w, t, u, v, x[o + 9], z, 2336552879),
            v = h(v, w, t, u, x[o + 10], A, 4294925233),
            u = h(u, v, w, t, x[o + 11], B, 2304563134),
            t = h(t, u, v, w, x[o + 12], y, 1804603682),
            w = h(w, t, u, v, x[o + 13], z, 4254626195),
            v = h(v, w, t, u, x[o + 14], A, 2792965006),
            u = h(u, v, w, t, x[o + 15], B, 1236535329),
            t = i(t, u, v, w, x[o + 1], C, 4129170786),
            w = i(w, t, u, v, x[o + 6], D, 3225465664),
            v = i(v, w, t, u, x[o + 11], E, 643717713),
            u = i(u, v, w, t, x[o + 0], F, 3921069994),
            t = i(t, u, v, w, x[o + 5], C, 3593408605),
            w = i(w, t, u, v, x[o + 10], D, 38016083),
            v = i(v, w, t, u, x[o + 15], E, 3634488961),
            u = i(u, v, w, t, x[o + 4], F, 3889429448),
            t = i(t, u, v, w, x[o + 9], C, 568446438),
            w = i(w, t, u, v, x[o + 14], D, 3275163606),
            v = i(v, w, t, u, x[o + 3], E, 4107603335),
            u = i(u, v, w, t, x[o + 8], F, 1163531501),
            t = i(t, u, v, w, x[o + 13], C, 2850285829),
            w = i(w, t, u, v, x[o + 2], D, 4243563512),
            v = i(v, w, t, u, x[o + 7], E, 1735328473),
            u = i(u, v, w, t, x[o + 12], F, 2368359562),
            t = j(t, u, v, w, x[o + 5], G, 4294588738),
            w = j(w, t, u, v, x[o + 8], H, 2272392833),
            v = j(v, w, t, u, x[o + 11], I, 1839030562),
            u = j(u, v, w, t, x[o + 14], J, 4259657740),
            t = j(t, u, v, w, x[o + 1], G, 2763975236),
            w = j(w, t, u, v, x[o + 4], H, 1272893353),
            v = j(v, w, t, u, x[o + 7], I, 4139469664),
            u = j(u, v, w, t, x[o + 10], J, 3200236656),
            t = j(t, u, v, w, x[o + 13], G, 681279174),
            w = j(w, t, u, v, x[o + 0], H, 3936430074),
            v = j(v, w, t, u, x[o + 3], I, 3572445317),
            u = j(u, v, w, t, x[o + 6], J, 76029189),
            t = j(t, u, v, w, x[o + 9], G, 3654602809),
            w = j(w, t, u, v, x[o + 12], H, 3873151461),
            v = j(v, w, t, u, x[o + 15], I, 530742520),
            u = j(u, v, w, t, x[o + 2], J, 3299628645),
            t = k(t, u, v, w, x[o + 0], K, 4096336452),
            w = k(w, t, u, v, x[o + 7], L, 1126891415),
            v = k(v, w, t, u, x[o + 14], M, 2878612391),
            u = k(u, v, w, t, x[o + 5], N, 4237533241),
            t = k(t, u, v, w, x[o + 12], K, 1700485571),
            w = k(w, t, u, v, x[o + 3], L, 2399980690),
            v = k(v, w, t, u, x[o + 10], M, 4293915773),
            u = k(u, v, w, t, x[o + 1], N, 2240044497),
            t = k(t, u, v, w, x[o + 8], K, 1873313359),
            w = k(w, t, u, v, x[o + 15], L, 4264355552),
            v = k(v, w, t, u, x[o + 6], M, 2734768916),
            u = k(u, v, w, t, x[o + 13], N, 1309151649),
            t = k(t, u, v, w, x[o + 4], K, 4149444226),
            w = k(w, t, u, v, x[o + 11], L, 3174756917),
            v = k(v, w, t, u, x[o + 2], M, 718787259),
            u = k(u, v, w, t, x[o + 9], N, 3951481745),
            t = c(t, p),
            u = c(u, q),
            v = c(v, r),
            w = c(w, s);
        var O = m(t) + m(u) + m(v) + m(w);
        return O.toLowerCase()
    }
    function i(a) {
        return "[object Object]" == {}.toString.call(a)
    }
    function j(a, b, c) {
        var d = c || {};
        document.cookie = a.replace(/[^+#$&^`|]/g, encodeURIComponent).replace("(", "%28").replace(")", "%29") + "=" + b.replace(/[^+#$&\/:<-\[\]-}]/g, encodeURIComponent) + (d.domain ? ";domain=" + d.domain : "") + (d.path ? ";path=" + d.path : "") + (d.secure ? ";secure" : "") + (d.httponly ? ";HttpOnly" : "") + (d.sameSite ? ";Samesite=" + d.sameSite : "")
    }
    function k(a) {
        var b = new RegExp("(?:^|;\\s*)" + a + "\\=([^;]+)(?:;\\s*|$)").exec(document.cookie);
        return b ? b[1] : void 0
    }
    function l(a, b, c) {
        var d = new Date;
        d.setTime(d.getTime() - 864e5);
        var e = "/";
        document.cookie = a + "=;path=" + e + ";domain=." + b + ";expires=" + d.toGMTString(),
        document.cookie = a + "=;path=" + e + ";domain=." + c + "." + b + ";expires=" + d.toGMTString()
    }
    function m(a, b) {
        for (var c = a.split("."), d = b.split("."), e = 3, f = 0; e > f; f++) {
            var g = Number(c[f])
              , h = Number(d[f]);
            if (g > h)
                return 1;
            if (h > g)
                return -1;
            if (!isNaN(g) && isNaN(h))
                return 1;
            if (isNaN(g) && !isNaN(h))
                return -1
        }
        return 0
    }
    function n() {
        var b = a.location.hostname;
        if (!b) {
            var c = a.parent.location.hostname;
            c && ~c.indexOf("zebra.alibaba-inc.com") && (b = c)
        }
        var d = ["taobao.net", "taobao.com", "tmall.com", "tmall.hk", "alibaba-inc.com"]
          , e = new RegExp("([^.]*?)\\.?((?:" + d.join(")|(?:").replace(/\./g, "\\.") + "))","i")
          , f = b.match(e) || []
          , g = f[2] || "taobao.com"
          , h = f[1] || "m";
        "taobao.net" !== g || "x" !== h && "waptest" !== h && "daily" !== h ? "taobao.net" === g && "demo" === h ? h = "demo" : "alibaba-inc.com" === g && "zebra" === h ? h = "zebra" : "waptest" !== h && "wapa" !== h && "m" !== h && (h = "m") : h = "waptest";
        var i = "h5api";
        "taobao.net" === g && "waptest" === h && (i = "acs"),
        s.mainDomain = g,
        s.subDomain = h,
        s.prefix = i
    }
    function o() {
        var b = a.navigator.userAgent
          , c = b.match(/WindVane[\/\s]([\d\.\_]+)/);
        c && (s.WindVaneVersion = c[1]);
        var d = b.match(/AliApp\(([^\/]+)\/([\d\.\_]+)\)/i);
        d && (s.AliAppName = d[1],
        s.AliAppVersion = d[2]);
        var e = b.match(/AMapClient\/([\d\.\_]+)/i);
        e && (s.AliAppName = "AMAP",
        s.AliAppVersion = e[1])
    }
    function p(a) {
        this.id = "" + (new Date).getTime() + ++y,
        this.params = d(a || {}, {
            v: "*",
            data: {},
            type: "get",
            dataType: "jsonp"
        }),
        this.params.type = this.params.type.toLowerCase(),
        "object" == typeof this.params.data && (this.params.data = JSON.stringify(this.params.data)),
        this.middlewares = t.slice(0)
    }
    var q = a.Promise
      , r = (q || {
        resolve: function() {
            return void 0
        }
    }).resolve();
    String.prototype.trim || (String.prototype.trim = function() {
        return this.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, "")
    }
    );
    var s = {
        useJsonpResultType: !1,
        safariGoLogin: !0,
        useAlipayJSBridge: !1
    }
      , t = []
      , u = {
        ERROR: -1,
        SUCCESS: 0,
        TOKEN_EXPIRED: 1,
        SESSION_EXPIRED: 2
    };
    n(),
    o();
    var v = /[Android|Adr]/.test(a.navigator.userAgent)
      , w = "AP" === s.AliAppName
      , x = w && m(s.AliAppVersion, "10.1.2") >= 0 || "KB" === s.AliAppName && m(s.AliAppVersion, "7.1.62") >= 0 || v && "AMAP" === s.AliAppName && m(s.AliAppVersion, "1.0.1") >= 0
      , y = 0
      , z = "2.6.1";
    p.prototype.use = function(a) {
        if (!a)
            throw new Error("middleware is undefined");
        return this.middlewares.push(a),
        this
    }
    ,
    p.prototype.__processRequestMethod = function(a) {
        var b = this.params
          , c = this.options;
        "get" === b.type && "jsonp" === b.dataType ? c.getJSONP = !0 : "get" === b.type && "originaljsonp" === b.dataType ? c.getOriginalJSONP = !0 : "get" === b.type && "json" === b.dataType ? c.getJSON = !0 : "post" === b.type && (c.postJSON = !0),
        a()
    }
    ,
    p.prototype.__processRequestType = function(c) {
        var d = this
          , e = this.params
          , f = this.options;
        if (s.H5Request === !0 && (f.H5Request = !0),
        s.WindVaneRequest === !0 && (f.WindVaneRequest = !0),
        f.H5Request === !1 && f.WindVaneRequest === !0) {
            if (!x && (!b.windvane || parseFloat(f.WindVaneVersion) < 5.4))
                throw new Error("WINDVANE_NOT_FOUND::缺少WindVane环境");
            if (x && !a.AlipayJSBridge)
                throw new Error("ALIPAY_NOT_READY::支付宝通道未准备好，支付宝请见 https://lark.alipay.com/mtbsdkdocs/mtopjssdkdocs/pucq6z")
        } else if (f.H5Request === !0)
            f.WindVaneRequest = !1;
        else if ("undefined" == typeof f.WindVaneRequest && "undefined" == typeof f.H5Request) {
            if (b.windvane && parseFloat(f.WindVaneVersion) >= 5.4 ? f.WindVaneRequest = !0 : f.H5Request = !0,
            x) {
                if (f.WindVaneRequest = f.H5Request = void 0,
                a.AlipayJSBridge)
                    if (i(e.data))
                        f.WindVaneRequest = !0;
                    else
                        try {
                            i(JSON.parse(e.data)) ? f.WindVaneRequest = !0 : f.H5Request = !0
                        } catch (g) {
                            f.H5Request = !0
                        }
                else
                    f.H5Request = !0;
                "AMAP" !== s.AliAppName || e.useNebulaJSbridgeWithAMAP || (f.WindVaneRequest = f.H5Request = void 0,
                f.H5Request = !0)
            }
            window.self !== window.top && (f.H5Request = !0)
        }
        var h = a.navigator.userAgent.toLowerCase();
        return h.indexOf("youku") > -1 && f.mainDomain.indexOf("youku.com") < 0 && (f.WindVaneRequest = !1,
        f.H5Request = !0),
        f.mainDomain.indexOf("youku.com") > -1 && h.indexOf("youku") < 0 && (f.WindVaneRequest = !1,
        f.H5Request = !0),
        c ? c().then(function() {
            var a = f.retJson.ret;
            if (a instanceof Array && (a = a.join(",")),
            f.WindVaneRequest === !0 && x && f.retJson.error || !a || a.indexOf("PARAM_PARSE_ERROR") > -1 || a.indexOf("HY_FAILED") > -1 || a.indexOf("HY_NO_HANDLER") > -1 || a.indexOf("HY_CLOSED") > -1 || a.indexOf("HY_EXCEPTION") > -1 || a.indexOf("HY_NO_PERMISSION") > -1) {
                if (!x || !isNaN(f.retJson.error) || -1 !== f.retJson.error.indexOf("FAIL_SYS_ACCESS_DENIED"))
                    return x && i(e.data) && (e.data = JSON.stringify(e.data)),
                    s.H5Request = !0,
                    d.__sequence([d.__processRequestType, d.__processToken, d.__processRequestUrl, d.middlewares, d.__processRequest]);
                "undefined" == typeof f.retJson.api && "undefined" == typeof f.retJson.v && (f.retJson.api = e.api,
                f.retJson.v = e.v,
                f.retJson.ret = [f.retJson.error + "::" + f.retJson.errorMessage],
                f.retJson.data = {})
            }
        }) : void 0
    }
    ;
    var A = "_m_h5_c"
      , B = "_m_h5_tk"
      , C = "_m_h5_tk_enc";
    p.prototype.__getTokenFromAlipay = function() {
        var b = c()
          , d = this.options
          , e = (a.navigator.userAgent,
        !!location.protocol.match(/^https?\:$/));
        return d.useAlipayJSBridge === !0 && !e && x && a.AlipayJSBridge && a.AlipayJSBridge.call ? a.AlipayJSBridge.call("getMtopToken", function(a) {
            a && a.token && (d.token = a.token),
            b.resolve()
        }, function() {
            b.resolve()
        }) : b.resolve(),
        b.promise
    }
    ,
    p.prototype.__getTokenFromCookie = function() {
        var a = this.options;
        return a.CDR && k(A) ? a.token = k(A).split(";")[0] : a.token = a.token || k(B),
        a.token && (a.token = a.token.split("_")[0]),
        q.resolve()
    }
    ,
    p.prototype.__waitWKWebViewCookie = function(b) {
        var c = this.options;
        c.waitWKWebViewCookieFn && c.H5Request && a.webkit && a.webkit.messageHandlers ? c.waitWKWebViewCookieFn(b) : b()
    }
    ,
    p.prototype.__processToken = function(a) {
        var b = this
          , c = this.options;
        this.params;
        return c.token && delete c.token,
        c.WindVaneRequest !== !0 ? r.then(function() {
            return b.__getTokenFromAlipay()
        }).then(function() {
            return b.__getTokenFromCookie()
        }).then(a).then(function() {
            var a = c.retJson
              , d = a.ret;
            if (d instanceof Array && (d = d.join(",")),
            d.indexOf("TOKEN_EMPTY") > -1 || (c.CDR === !0 || c.syncCookieMode === !0) && d.indexOf("ILLEGAL_ACCESS") > -1 || d.indexOf("TOKEN_EXOIRED") > -1) {
                if (c.maxRetryTimes = c.maxRetryTimes || 5,
                c.failTimes = c.failTimes || 0,
                c.H5Request && ++c.failTimes < c.maxRetryTimes) {
                    var e = [b.__waitWKWebViewCookie, b.__processToken, b.__processRequestUrl, b.middlewares, b.__processRequest];
                    if (c.syncCookieMode === !0 && b.constructor.__cookieProcessorId !== b.id)
                        if (b.constructor.__cookieProcessor) {
                            var f = function(a) {
                                var c = function() {
                                    b.constructor.__cookieProcessor = null,
                                    b.constructor.__cookieProcessorId = null,
                                    a()
                                };
                                b.constructor.__cookieProcessor ? b.constructor.__cookieProcessor.then(c)["catch"](c) : a()
                            };
                            e = [f, b.__waitWKWebViewCookie, b.__processToken, b.__processRequestUrl, b.middlewares, b.__processRequest]
                        } else
                            b.constructor.__cookieProcessor = b.__requestProcessor,
                            b.constructor.__cookieProcessorId = b.id;
                    return b.__sequence(e)
                }
                c.maxRetryTimes > 0 && (l(A, c.pageDomain, "*"),
                l(B, c.mainDomain, c.subDomain),
                l(C, c.mainDomain, c.subDomain)),
                a.retType = u.TOKEN_EXPIRED
            }
        }) : void a()
    }
    ,
    p.prototype.__processRequestUrl = function(b) {
        var c = this.params
          , d = this.options;
        if (d.hostSetting && d.hostSetting[a.location.hostname]) {
            var e = d.hostSetting[a.location.hostname];
            e.prefix && (d.prefix = e.prefix),
            e.subDomain && (d.subDomain = e.subDomain),
            e.mainDomain && (d.mainDomain = e.mainDomain)
        }
        if (d.H5Request === !0) {
            var f = "//" + (d.prefix ? d.prefix + "." : "") + (d.subDomain ? d.subDomain + "." : "") + d.mainDomain + "/h5/" + c.api.toLowerCase() + "/" + c.v.toLowerCase() + "/"
              , g = c.appKey || ("waptest" === d.subDomain ? "4272" : "12574478")
              , i = (new Date).getTime()
              , j = h(d.token + "&" + i + "&" + g + "&" + c.data)
              , k = {
                jsv: z,
                appKey: g,
                t: i,
                sign: j
            }
              , l = {
                data: c.data,
                ua: c.ua
            };
            Object.keys(c).forEach(function(a) {
                "undefined" == typeof k[a] && "undefined" == typeof l[a] && "headers" !== a && "ext_headers" !== a && "ext_querys" !== a && (k[a] = c[a])
            }),
            c.ext_querys && Object.keys(c.ext_querys).forEach(function(a) {
                k[a] = c.ext_querys[a]
            }),
            d.getJSONP ? k.type = "jsonp" : d.getOriginalJSONP ? k.type = "originaljsonp" : (d.getJSON || d.postJSON) && (k.type = "originaljson"),
            "undefined" != typeof c.valueType && ("original" === c.valueType ? d.getJSONP || d.getOriginalJSONP ? k.type = "originaljsonp" : (d.getJSON || d.postJSON) && (k.type = "originaljson") : "string" === c.valueType && (d.getJSONP || d.getOriginalJSONP ? k.type = "jsonp" : (d.getJSON || d.postJSON) && (k.type = "json"))),
            d.useJsonpResultType === !0 && "originaljson" === k.type && delete k.type,
            d.dangerouslySetProtocol && (f = d.dangerouslySetProtocol + ":" + f),
            d.querystring = k,
            d.postdata = l,
            d.path = f
        }
        b()
    }
    ,
    p.prototype.__processUnitPrefix = function(a) {
        a()
    }
    ;
    var D = 0;
    p.prototype.__requestJSONP = function(a) {
        function b(a) {
            if (k && clearTimeout(k),
            l.parentNode && l.parentNode.removeChild(l),
            "TIMEOUT" === a)
                window[j] = function() {
                    window[j] = void 0;
                    try {
                        delete window[j]
                    } catch (a) {}
                }
                ;
            else {
                window[j] = void 0;
                try {
                    delete window[j]
                } catch (b) {}
            }
        }
        var d = c()
          , g = this.params
          , h = this.options
          , i = g.timeout || 2e4
          , j = "mtopjsonp" + (g.jsonpIncPrefix || "") + ++D
          , k = setTimeout(function() {
            a(h.timeoutErrMsg || "TIMEOUT::接口超时"),
            b("TIMEOUT")
        }, i);
        h.querystring.callback = j;
        var l = document.createElement("script");
        return l.src = h.path + "?" + f(h.querystring) + "&" + f(h.postdata),
        l.async = !0,
        l.onerror = function() {
            b("ABORT"),
            a(h.abortErrMsg || "ABORT::接口异常退出")
        }
        ,
        window[j] = function() {
            h.results = Array.prototype.slice.call(arguments),
            b(),
            d.resolve()
        }
        ,
        e(l),
        d.promise
    }
    ,
    p.prototype.__requestJSON = function(b) {
        function d(a) {
            l && clearTimeout(l),
            "TIMEOUT" === a && i.abort()
        }
        var e = c()
          , g = this.params
          , h = this.options
          , i = new a.XMLHttpRequest
          , j = g.timeout || 2e4
          , l = setTimeout(function() {
            b(h.timeoutErrMsg || "TIMEOUT::接口超时"),
            d("TIMEOUT")
        }, j);
        h.CDR && k(A) && (h.querystring.c = decodeURIComponent(k(A))),
        i.onreadystatechange = function() {
            if (4 == i.readyState) {
                var a, c, f = i.status;
                if (f >= 200 && 300 > f || 304 == f) {
                    d(),
                    a = i.responseText,
                    c = i.getAllResponseHeaders() || "";
                    try {
                        a = /^\s*$/.test(a) ? {} : JSON.parse(a),
                        a.responseHeaders = c,
                        h.results = [a],
                        e.resolve()
                    } catch (g) {
                        b("PARSE_JSON_ERROR::解析JSON失败")
                    }
                } else
                    d("ABORT"),
                    b(h.abortErrMsg || "ABORT::接口异常退出")
            }
        }
        ;
        var m, n, o = h.path + "?" + f(h.querystring);
        h.getJSON ? (m = "GET",
        o += "&" + f(h.postdata)) : h.postJSON && (m = "POST",
        n = f(h.postdata)),
        i.open(m, o, !0),
        i.withCredentials = !0,
        i.setRequestHeader("Accept", "application/json"),
        i.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        var p = g.ext_headers || g.headers;
        if (p)
            for (var q in p)
                i.setRequestHeader(q, p[q]);
        return i.send(n),
        e.promise
    }
    ,
    p.prototype.__requestWindVane = function(a) {
        function d(a) {
            g.results = [a],
            e.resolve()
        }
        var e = c()
          , f = this.params
          , g = this.options
          , h = f.data
          , i = f.api
          , j = f.v
          , k = g.postJSON ? 1 : 0
          , l = g.getJSON || g.postJSON || g.getOriginalJSONP ? "originaljson" : "";
        "undefined" != typeof f.valueType && ("original" === f.valueType ? l = "originaljson" : "string" === f.valueType && (l = "")),
        g.useJsonpResultType === !0 && (l = "");
        var m, n, o = "https" === location.protocol ? 1 : 0, p = f.isSec || 0, q = f.sessionOption || "AutoLoginOnly", r = f.ecode || 0, s = f.ext_headers || {}, t = f.ext_querys || {};
        n = "undefined" != typeof f.timer ? parseInt(f.timer) : "undefined" != typeof f.timeout ? parseInt(f.timeout) : 2e4,
        m = 2 * n,
        f.needLogin === !0 && "undefined" == typeof f.sessionOption && (q = "AutoLoginAndManualLogin"),
        "undefined" != typeof f.secType && "undefined" == typeof f.isSec && (p = f.secType);
        var u = {
            api: i,
            v: j,
            post: String(k),
            type: l,
            isHttps: String(o),
            ecode: String(r),
            isSec: String(p),
            param: JSON.parse(h),
            timer: n,
            sessionOption: q,
            ext_headers: s,
            ext_querys: t
        };
        f.ttid && g.dangerouslySetWVTtid === !0 && (u.ttid = f.ttid),
        Object.assign && f.dangerouslySetWindvaneParams && Object.assign(u, f.dangerouslySetWindvaneParams);
        var v = "MtopWVPlugin";
        return "string" == typeof f.customWindVaneClassName && (v = f.customWindVaneClassName),
        b.windvane.call(v, "send", u, d, d, m),
        e.promise
    }
    ,
    p.prototype.__requestAlipay = function(b) {
        function d(a) {
            g.results = [a],
            e.resolve()
        }
        var e = c()
          , f = this.params
          , g = this.options
          , h = {
            apiName: f.api,
            apiVersion: f.v,
            needEcodeSign: "1" === String(f.ecode),
            headers: f.ext_headers || {},
            usePost: !!g.postJSON
        };
        i(f.data) || (f.data = JSON.parse(f.data)),
        h.data = f.data,
        f.ttid && g.dangerouslySetWVTtid === !0 && (h.ttid = f.ttid),
        (g.getJSON || g.postJSON || g.getOriginalJSONP) && (h.type = "originaljson"),
        "undefined" != typeof f.valueType && ("original" === f.valueType ? h.type = "originaljson" : "string" === f.valueType && delete h.type),
        g.useJsonpResultType === !0 && delete h.type,
        Object.assign && f.dangerouslySetAlipayParams && Object.assign(h, f.dangerouslySetAlipayParams);
        var j = "mtop";
        return "string" == typeof f.customAlipayJSBridgeApi && (j = f.customAlipayJSBridgeApi),
        a.AlipayJSBridge.call(j, h, d),
        e.promise
    }
    ,
    p.prototype.__processRequest = function(a, b) {
        var c = this;
        return r.then(function() {
            var a = c.options;
            if (a.H5Request && (a.getJSONP || a.getOriginalJSONP))
                return c.__requestJSONP(b);
            if (a.H5Request && (a.getJSON || a.postJSON))
                return c.__requestJSON(b);
            if (a.WindVaneRequest)
                return x ? c.__requestAlipay(b) : c.__requestWindVane(b);
            throw new Error("UNEXCEPT_REQUEST::错误的请求类型")
        }).then(a).then(function() {
            var a = c.options
              , b = (c.params,
            a.results[0])
              , d = b && b.ret || [];
            b.ret = d,
            d instanceof Array && (d = d.join(","));
            var e = b.c;
            a.CDR && e && j(A, e, {
                domain: a.pageDomain,
                path: "/",
                secure: a.secure,
                sameSite: a.sameSite
            }),
            d.indexOf("SUCCESS") > -1 ? b.retType = u.SUCCESS : b.retType = u.ERROR,
            a.retJson = b
        })
    }
    ,
    p.prototype.__sequence = function(a) {
        function b(a) {
            if (a instanceof Array)
                a.forEach(b);
            else {
                var g, h = c(), i = c();
                e.push(function() {
                    return h = c(),
                    g = a.call(d, function(a) {
                        return h.resolve(a),
                        i.promise
                    }, function(a) {
                        return h.reject(a),
                        i.promise
                    }),
                    g && (g = g["catch"](function(a) {
                        h.reject(a)
                    })),
                    h.promise
                }),
                f.push(function(a) {
                    return i.resolve(a),
                    g
                })
            }
        }
        var d = this
          , e = []
          , f = [];
        a.forEach(b);
        for (var g, h = r; g = e.shift(); )
            h = h.then(g);
        for (; g = f.pop(); )
            h = h.then(g);
        return h
    }
    ;
    var E = function(a) {
        a()
    }
      , F = function(a) {
        a()
    };
    p.prototype.request = function(c) {
        var e = this;
        if (this.options = d(c || {}, s),
        !q) {
            var f = "当前浏览器不支持Promise，请在windows对象上挂载Promise对象";
            throw b.mtop = {
                ERROR: f
            },
            new Error(f)
        }
        var h = q.resolve([E, F]).then(function(a) {
            var b = a[0]
              , c = a[1];
            return e.__sequence([b, e.__processRequestMethod, e.__processRequestType, e.__processToken, e.__processRequestUrl, e.middlewares, e.__processRequest, c])
        }).then(function() {
            var a = e.options.retJson;
            return a.retType !== u.SUCCESS ? q.reject(a) : e.options.successCallback ? void e.options.successCallback(a) : q.resolve(a)
        })["catch"](function(a) {
            var c;
            return a instanceof Error ? (console.error(a.stack),
            c = {
                ret: [a.message],
                stack: [a.stack],
                retJson: u.ERROR
            }) : c = "string" == typeof a ? {
                ret: [a],
                retJson: u.ERROR
            } : void 0 !== a ? a : e.options.retJson,
            b.mtop.errorListener && b.mtop.errorListener({
                api: e.params.api,
                data: e.params.data,
                v: e.params.v,
                retJson: c
            }),
            e.options.failureCallback ? void e.options.failureCallback(c) : q.reject(c)
        });
        return this.__processRequestType(),
        e.options.H5Request && (e.constructor.__firstProcessor || (e.constructor.__firstProcessor = h),
        E = function(a) {
            e.constructor.__firstProcessor.then(a)["catch"](a)
        }
        ),
        ("get" === this.params.type && "json" === this.params.dataType || "post" === this.params.type) && (c.pageDomain = c.pageDomain || g(a.location.hostname),
        c.mainDomain !== c.pageDomain && (c.maxRetryTimes = 4,
        c.CDR = !0)),
        this.__requestProcessor = h,
        h
    }
    ,
    b.mtop = function(a) {
        return new p(a)
    }
    ,
    b.mtop.request = function(a, b, c) {
        var d = {
            H5Request: a.H5Request,
            WindVaneRequest: a.WindVaneRequest,
            LoginRequest: a.LoginRequest,
            AntiCreep: a.AntiCreep,
            AntiFlood: a.AntiFlood,
            successCallback: b,
            failureCallback: c || b
        };
        return new p(a).request(d)
    }
    ,
    b.mtop.H5Request = function(a, b, c) {
        var d = {
            H5Request: !0,
            successCallback: b,
            failureCallback: c || b
        };
        return new p(a).request(d)
    }
    ,
    b.mtop.middlewares = t,
    b.mtop.config = s,
    b.mtop.RESPONSE_TYPE = u,
    b.mtop.CLASS = p
}(window, window.lib || (window.lib = {})),
function(a, b) {
    function c(a) {
        return a.preventDefault(),
        !1
    }
    function d(a) {
        var b = new RegExp("(?:^|;\\s*)" + a + "\\=([^;]+)(?:;\\s*|$)").exec(document.cookie);
        return b ? b[1] : void 0
    }
    function e(b, d) {
        var e = this
          , f = a.dpr || 1
          , g = document.createElement("div")
          , h = document.documentElement.getBoundingClientRect()
          , i = Math.max(h.width, window.innerWidth) / f
          , j = Math.max(h.height, window.innerHeight) / f;
        g.style.cssText = ["-webkit-transform:scale(" + f + ") translateZ(0)", "-ms-transform:scale(" + f + ") translateZ(0)", "transform:scale(" + f + ") translateZ(0)", "-webkit-transform-origin:0 0", "-ms-transform-origin:0 0", "transform-origin:0 0", "width:" + i + "px", "height:" + j + "px", "z-index:2147483647", "position:" + (i > 800 ? "fixed" : "absolute"), "left:0", "top:0px", "background:" + (i > 800 ? "rgba(0,0,0,.5)" : "#FFF"), "display:none"].join(";");
        var k = document.createElement("div");
        k.style.cssText = ["width:100%", "height:52px", "background:#EEE", "line-height:52px", "text-align:left", "box-sizing:border-box", "padding-left:20px", "position:absolute", "left:0", "top:0", "font-size:16px", "font-weight:bold", "color:#333"].join(";"),
        k.innerText = b;
        var l = navigator.userAgent.match(/.*(iPhone|iPad|Android|ios|SymbianOS|Windows Phone).*/i)
          , m = document.createElement("img");
        m.style.cssText = ["display:block", "position:absolute", "margin-top:15px", "right:0", "top:0", "height:15px", "line-height:52px", "padding:0 20px", "color:#999"].join(";"),
        m.src = "https://gw.alicdn.com/tfs/TB1QZN.CYj1gK0jSZFuXXcrHpXa-200-200.png";
        var n = document.createElement("iframe");
        n.style.cssText = ["width:100%", "height:100%", "border:0", "overflow:hidden"].join(";"),
        l ? (k.appendChild(m),
        g.appendChild(k)) : (m.style.cssText = ["position:absolute", "width:15px", "height:15px", "top:102px", "left:" + (i / 2 - 185 + 390) + "px", "cursor: pointer", "border:0", "z-index:1", "overflow:hidden"].join(";"),
        g.appendChild(m),
        n.style.cssText = ["position:absolute", "top:92px", "left:" + (i / 2 - 185) + "px", "width:420px", "height:320px", "border:0", "background:#FFF", "overflow:hidden"].join(";")),
        g.appendChild(n),
        g.className = "J_MIDDLEWARE_FRAME_WIDGET",
        document.body.appendChild(g),
        n.src = d,
        m.addEventListener("click", function() {
            e.hide();
            var a = document.createEvent("HTMLEvents");
            a.initEvent("close", !1, !1),
            g.dispatchEvent(a)
        }, !1),
        this.addEventListener = function() {
            g.addEventListener.apply(g, arguments)
        }
        ,
        this.removeEventListener = function() {
            g.removeEventListener.apply(g, arguments)
        }
        ,
        this.show = function() {
            document.addEventListener("touchmove", c, !1),
            g.style.display = "block",
            window.scrollTo(0, 0)
        }
        ,
        this.hide = function() {
            document.removeEventListener("touchmove", c),
            window.scrollTo(0, -h.top),
            g.parentNode && g.parentNode.removeChild(g)
        }
    }
    function f(a) {
        var c = this
          , d = this.options
          , e = this.params;
        return a().then(function() {
            var a = d.retJson
              , f = a.ret
              , g = navigator.userAgent.toLowerCase()
              , h = g.indexOf("safari") > -1 && g.indexOf("chrome") < 0 && g.indexOf("qqbrowser") < 0;
            if (f instanceof Array && (f = f.join(",")),
            (f.indexOf("SESSION_EXPIRED") > -1 || f.indexOf("SID_INVALID") > -1 || f.indexOf("AUTH_REJECT") > -1 || f.indexOf("NEED_LOGIN") > -1) && (a.retType = l.SESSION_EXPIRED,
            !d.WindVaneRequest && (k.LoginRequest === !0 || d.LoginRequest === !0 || e.needLogin === !0))) {
                if (!b.login)
                    throw new Error("LOGIN_NOT_FOUND::缺少lib.login");
                if (d.safariGoLogin !== !0 || !h || "taobao.com" === d.pageDomain)
                    return b.login.goLoginAsync().then(function(a) {
                        return c.__sequence([c.__processToken, c.__processRequestUrl, c.__processUnitPrefix, c.middlewares, c.__processRequest])
                    })["catch"](function(a) {
                        throw "CANCEL" === a ? new Error("LOGIN_CANCEL::用户取消登录") : new Error("LOGIN_FAILURE::用户登录失败")
                    });
                b.login.goLogin()
            }
        })
    }
    function g(a) {
        var b = this.options;
        this.params;
        return b.H5Request !== !0 || k.AntiFlood !== !0 && b.AntiFlood !== !0 ? void a() : a().then(function() {
            var a = b.retJson
              , c = a.ret;
            c instanceof Array && (c = c.join(",")),
            c.indexOf("FAIL_SYS_USER_VALIDATE") > -1 && a.data.url && (b.AntiFloodReferer ? location.href = a.data.url.replace(/(http_referer=).+/, "$1" + b.AntiFloodReferer) : location.href = a.data.url)
        })
    }
    function h(b) {
        var c = this
          , f = this.options
          , g = this.params;
        return f.AntiCreep !== !1 && (f.AntiCreep = !0),
        g.forceAntiCreep !== !0 && f.H5Request !== !0 || k.AntiCreep !== !0 && f.AntiCreep !== !0 ? void b() : b().then(function() {
            var b = f.retJson
              , h = b.ret;
            if (h instanceof Array && (h = h.join(",")),
            (h.indexOf("RGV587_ERROR::SM") > -1 || h.indexOf("ASSIST_FLAG") > -1) && b.data.url) {
                var j = "_m_h5_smt"
                  , k = d(j)
                  , l = !1;
                if (f.saveAntiCreepToken === !0 && k) {
                    k = JSON.parse(k);
                    for (var m in k)
                        g[m] && (l = !0)
                }
                if (f.saveAntiCreepToken === !0 && k && !l) {
                    for (var m in k)
                        g[m] = k[m];
                    return c.__sequence([c.__processToken, c.__processRequestUrl, c.__processUnitPrefix, c.middlewares, c.__processRequest])
                }
                return new i(function(d, h) {
                    function i() {
                        m.removeEventListener("close", i),
                        a.removeEventListener("message", k),
                        h("USER_INPUT_CANCEL::用户取消输入")
                    }
                    function k(b) {
                        var e;
                        try {
                            e = JSON.parse(b.data) || {}
                        } catch (l) {}
                        if (e && "child" === e.type) {
                            m.removeEventListener("close", i),
                            a.removeEventListener("message", k),
                            m.hide();
                            var n;
                            try {
                                n = JSON.parse(decodeURIComponent(e.content)),
                                "string" == typeof n && (n = JSON.parse(n));
                                for (var o in n)
                                    g[o] = n[o];
                                f.saveAntiCreepToken === !0 ? (document.cookie = j + "=" + JSON.stringify(n) + ";",
                                a.location.reload()) : c.__sequence([c.__processToken, c.__processRequestUrl, c.__processUnitPrefix, c.middlewares, c.__processRequest]).then(d)
                            } catch (l) {
                                h("USER_INPUT_FAILURE::用户输入失败")
                            }
                        }
                    }
                    var l = b.data.url
                      , m = new e("",l);
                    m.addEventListener("close", i, !1),
                    a.addEventListener("message", k, !1),
                    m.show()
                }
                )
            }
        })
    }
    if (!b || !b.mtop || b.mtop.ERROR)
        throw new Error("Mtop 初始化失败！");
    var i = a.Promise
      , j = b.mtop.CLASS
      , k = b.mtop.config
      , l = b.mtop.RESPONSE_TYPE;
    b.mtop.middlewares.push(f),
    b.mtop.loginRequest = function(a, b, c) {
        var d = {
            LoginRequest: !0,
            H5Request: !0,
            successCallback: b,
            failureCallback: c || b
        };
        return new j(a).request(d)
    }
    ,
    b.mtop.antiFloodRequest = function(a, b, c) {
        var d = {
            AntiFlood: !0,
            successCallback: b,
            failureCallback: c || b
        };
        return new j(a).request(d)
    }
    ,
    b.mtop.middlewares.push(g),
    b.mtop.antiCreepRequest = function(a, b, c) {
        var d = {
            AntiCreep: !0,
            successCallback: b,
            failureCallback: c || b
        };
        return new j(a).request(d)
    }
    ,
    b.mtop.middlewares.push(h)
}(window, window.lib || (window.lib = {}));
(()=>{
    var e, n, o, i;
    window.$$pageSeed.combine = location.search.indexOf("_debugMode_=1") < 0,
    window.g_config = window.g_config || {},
    window.g_config.seed = window.$$pageSeed,
    window.require.config(window.$$pageSeed),
    window._objectWithoutPropertiesLoose || (window._objectWithoutPropertiesLoose = function(e, n) {
        if (null == e)
            return {};
        var o, i, t = {}, r = Object.keys(e);
        for (i = 0; i < r.length; i++)
            o = r[i],
            n.indexOf(o) >= 0 || (t[o] = e[o]);
        return t
    }
    ),
    window._interopRequireDefault || (window._interopRequireDefault = function(e) {
        return e && e.__esModule ? e : {
            default: e
        }
    }
    );
    var t = null !== (e = window.__supportsES6) && void 0 !== e ? e : function() {
        try {
            return new Function("(a = 0) => a"),
            new Function("let a = {...{} }"),
            new Function("(function(a){for(let a = 1; a < 2; a++){} })(1)"),
            new Function("var a = async function() { return ''}"),
            !0
        } catch (e) {
            return !1
        }
    }();
    window.__supportsES6 = t,
    u("beforeSalexInit");
    var r = (null === (n = window) || void 0 === n || null === (o = n.$$pageSchema) || void 0 === o || null === (i = o.attributes) || void 0 === i ? void 0 : i.client.indexOf("pc")) < 0 && t ? "index-es6" : "index";
    function u(e) {
        try {
            var n = window[e];
            "function" == typeof n && n()
        } catch (e) {
            console.log(e)
        }
    }
    window.require(["@ali/rox-sale-page-init/" + r], (function(e) {
        _interopRequireDefault(e).default.render(),
        u("afterSalexInit")
    }
    ))
}
)();
