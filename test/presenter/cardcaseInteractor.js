'use strict'

/**
 * wechat app presenter simple sample
 */
export default class cardcaseInteractor {

    constructor(app, page, model) {
        this.app = app;
        this.view = page;
        this.model = model;
        this.nextId = "";
        this.lastPage = false;
        this.isPullDownRefreshing = false;
    }

    onLoad(options) {
        this.app.subscribe("cardCaseNotification", this.refresh);
        this.app.subscribe("loginNotification", this.refresh);
        this.app.subscribe("createBusinessCardSuccessNotification", this.checkLoginStatus);
        // 初始化时刷新数据
        this.refresh();
    }

    onShow() {
        this.getCardCount();
    }

    onUnload(options) {
        this.app.unSubscribe("loginNotification", this.refresh);
        this.app.unSubscribe("cardCaseNotification", this.refresh);
        this.app.unSubscribe("createBusinessCardSuccessNotification", this.checkLoginStatus);
    }

    // 监听登录状态 在切换用户时 正和岛用户登录成功需要重新刷新页面 失败则滞空
    checkLoginStatus() {
        var that = this;
        switch (this.app.loginStatus()) {
            case 1:
            case 2:
            case 3:
                that.nextId = "";
                that.lastPage = false;
                that.view.setPageData([], {"url": "../../common/images/img_empty_package.png", "name": "你还没有收藏任何名片"}, 0)
                break
            case 4:
                that.refresh();
                break;
        }
    }

    onReady(options) {
    }

    onPullDownRefresh() {
        this.isPullDownRefreshing = true;
    }

    onReachBottom(cardCount) {
        if (cardCount > 0 && !this.isPullDownRefreshing && !this.lastPage) {
            this.getListData(this.nextId);
        }
    }

    refresh() {
        this.getListData("");
    }

    getCardCount() {
        var that = this;
        this.model
            .getBizcardCount()
            .then(requestCount => {
                that.view
                    .setRequestCount(requestCount);
            });
    }

    getListData(nextId) {
        var that = this;
        this
            .view
            .startPullToRefreshAnim();
        this.model
            .getListData(nextId)
            .then(res => {
                that
                    .view
                    .stopPullToRefreshAnim(nextId == "");
                that
                    .view
                    .setDataToList(nextId == "", res);
                that.nextId = res.data.nextId,
                    that.lastPage = res.data.lastPage
            })
            .catch(err => {
                that
                    .view
                    .stopPullToRefreshAnim(nextId);
                that.isPullDownRefreshing = false;
            });
    }

    clickStar(item) {
        if (item.collected) {
            // 判断是否已经收藏
            // 弹窗点击确定取消收藏
            this
                .view
                .showDialog(item);
        }
    }

    cancelStar(item) {
        var that = this;
        this.model
            .cancelStar(item)
            .then(res => {
                // 遍历删除指定元素
                that.view.deleteItem(item);
                that.cardcaviewsePage.updataList(list);
                that.view.showLoadingToast("已取消收藏");
            });
    }

    onHeaderClick() {
        this.app.gotoUri('/pages/tobeconfirmed/tobeconfirmed');
    }

    onItemClicked(cardId) {
        this.app.gotoUri('/pages/othercard/othercard?cardId=' + cardId + "&fromLocal=" + true);
    }
}