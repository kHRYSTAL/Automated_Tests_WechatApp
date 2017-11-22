/**
 * Created by kHRYSTAL on 17/11/21.
 */

// mocha cardcaseInteractor.test.js --compilers js:babel-core/register
// mocha cardcaseInteractor.test.js --compilers js:babel-core/register -R doc > spec.html
import cardcaseInteractor from '../cardcaseInteractor';
import chai from 'chai';
import sinon from 'sinon';
let expect = chai.expect;

var app = {
        // global event inject
        subscribe: function (key, handler) {
        },
        unSubscribe: function () {
        },
        loginStatus: function () {
        },
        gotoUri(uri) {
        }
    },
    model = {
        getBizcardCount: function () {
        }
    }
    ,
    view = {
        setRequestCount: function () {
        }
    };


/**
 * Test case sample
 */
describe('cardcaseInteractor test case', function () {
    "use strict";
    var instance;

    beforeEach(function () {
        instance = new cardcaseInteractor(app, view, model);
    });

    afterEach(function () {
    });

    it('#onLoad', function () {
        "use strict";
        sinon.spy(app, 'subscribe');
        sinon.stub(instance, 'refresh');
        instance.onLoad();
        expect(app.subscribe.called);
        expect(instance.refresh.called);
    });

    it('#onShow', function () {
        "use strict";
        sinon.stub(instance, 'getCardCount');
        instance.onShow();
        expect(instance.getCardCount.called);
    });


    it('#refresh View', function () {
        let count = {};
        sinon.spy(view, 'setRequestCount');
        sinon.stub(model, 'getBizcardCount').resolves(count);
        instance.getCardCount();
        expect(view.setRequestCount.calledOn(count));
    });

    it('#onPullDownRefresh', function () {
        "use strict";
        instance.onPullDownRefresh();
        expect(instance.isPullDownRefreshing).to.equal(true);
    });

    it('#onReachBottom', function () {
        "use strict";
        sinon.stub(instance, 'getListData');
        instance.nextId = 2;
        instance.isPullDownRefreshing = false;
        instance.lastPage = false;
        instance.onReachBottom(1);
        expect(instance.getListData.calledOn(2));
    });

    it('#onUnload', function () {
        sinon.spy(app, 'unSubscribe');
        instance.onUnload();
        expect(app.unSubscribe.called);
    });
});

