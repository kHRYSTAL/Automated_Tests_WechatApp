/**
 * Created by kHRYSTAL on 17/11/21.
 */
function App(obj) {
    console.log("init app");
}

App({
    onLaunch(options) {

    },
    globalData: {
        eventbus: eb.eventbus,
        basicIntegrity: false,
        tagIntegrity: false,
        zhsession: "",
        userInfo: undefined,
        cardDetail: undefined,
        loginStatus: -1
    },

    getCardDetail: function (data) {
        console.log("getCardDetail")
    }


});