/**
 * Created by kHRYSTAL on 17/11/21.
 */

// mocha cardcaseInteractor.test.js --compilers js:babel-core/register
// mocha cardcaseInteractor.test.js --compilers js:babel-core/register -R doc > spec.html

import cardcaseInteractor from '../cardcaseInteractor';
var expect = require('chai').expect;
var sinon = require('sinon');


describe('cardcase函数测试', function () {
    it('测试生命周期onLoad', function () {
        var page = {};
        var options = new Object();
        let instance = new cardcaseInteractor(page);
        expect(instance.onLoad(options)).to.not.be.ok;
    });
});


// 

