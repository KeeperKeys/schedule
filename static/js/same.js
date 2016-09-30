function fib2(n) {
    var f1, f2 = 0;
    var f = 0;
    if (n >= 0) {
        for (var i = 0; i <= n; i++) {
            if (i == 0) {
                f2 = i; //f-2
                f = i;
            }
            if (i == 1) {
                f1 = i; //f-1
                f = i;
            }
            else if (i >= 2) {
                f = f1 + f2; //fn = f-1 + f-2
                f2 = f1;
                f1 = f;
            }
        }
    }
    else {
        for (var j = -1; j >= n; j--) {
            if (j == -1) f2 = 1; //f+2
            if (j == -2) f1 = -1; //f+1
            else {
                f = f2 - f1; //fn = f+2 - f+1
                f2 = f1;
                f1 = f;
            }
        }

    }
    return f;
}
//alert(fib2(10));
function fib_new(n) {
    var n_abs = Math.abs(n);
    if (n_abs > 2) {
        var a1 = 1;
        var a2 = 1;
        var res = 1;
        for (var i = 3; i <= n_abs; i++) {
            res = a1 + a2;
            a1 = a2;
            a2 = res;
        }
    }
    if (n_abs == 0) res = 0;
    if (n_abs == 1) res = 1;
    if (n_abs == 2) res = 2;
    if (n >= 0) return res;
    else return -res;
}

//alert(fib_new(-4));

var a = 4.8;
a = a^0;
alert(a);