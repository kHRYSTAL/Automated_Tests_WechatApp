/**
 * Created by kHRYSTAL on 17/11/21.
 */

// mocha cardcaseInteractor.test.js --compilers js:babel-core/register
// mocha cardcaseInteractor.test.js --compilers js:babel-core/register -R doc > spec.html

import cardcaseInteractor from '../cardcaseInteractor';
var expect = require('chai').expect;


describe('cardcase函数测试', function () {
    it('测试生命周期onLoad', function () {
        var page = {};
        var options = new Object();
        let instance = new cardcaseInteractor(page);
        expect(instance.onLoad(options)).to.not.be.ok;
    });
});


describe("refresh card", function () {
    it('测试数据为空', function () {
        let fakeServer = sinon.fakeServer.create();
        fakeServer.responseWith("GET", "/users", [
            200,
            {'Content-Type': 'application/json'},
            '[]'
        ])

        var appSpy = spyOn();
        var pageSpy = {};
        var options = new Object();
        let instance = new cardcaseInteractor(appSpy, pageSpy);

        instance.refresh();
        assert(pageSpy)

    });
    it('测试接口错误', function () {

    });
    it('测试数据只有一页数据', function () {

    });
    it('测试数据还有下一页', function () {

    });

})
