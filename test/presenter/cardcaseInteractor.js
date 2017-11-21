'use strict'

import eventbusKey from '../../util/eventbuskey';
import cardcaseservice from './cardcaseservice';
import loginType from '../../service/login/logintype';

export default class cardcaseInteractor {

  constructor(app, page) {
    this.app = app;
    this.cardcasePage = page;
    this.nextId = "";
    this.lastPage = false;
    this.isPullDownRefreshing = false;
    this.cardcaseservice = new cardcaseservice();
  }

  onLoad(options) {
    this.app
      .globalData
      .eventbus
      .subscribe(eventbusKey.cardCaseNotification, this.refresh);
    this.app
      .globalData
      .eventbus
      .subscribe(eventbusKey.loginNotification, this.refresh);
    this.app.globalData.eventbus.subscribe(eventbusKey.createBusinessCardSuccessNotification, this.checkLoginStatus);
    // 初始化时刷新数据
    this.refresh();
  }

  onShow() {
    this.getCardCount();
  }

  onUnload(options) {
    this.app
      .globalData
      .eventbus
      .unSubscribe(eventbusKey.loginNotification, this.refresh);
    getApp()
      .globalData
      .eventbus
      .unSubscribe(eventbusKey.cardCaseNotification, this.refresh);
    getApp()
      .globalData
      .eventbus
      .unSubscribe(eventbusKey.createBusinessCardSuccessNotification, this.checkLoginStatus);
  }

  // 监听登录状态 在切换用户时 正和岛用户登录成功需要重新刷新页面 失败则滞空
  checkLoginStatus() {
    var that = this;
    switch (getApp().globalData.loginStatus) {
      case loginType.wxloginFailed:
      case loginType.zhloginFailed:
      case loginType.getCardDetailFailed:
        that.nextId = "";
        that.lastPage = false;
        that.cardcasePage.setPageData([], { "url": "../../common/images/img_empty_package.png", "name": "你还没有收藏任何名片" }, 0)
        break
      case loginType.zhloginSuccess:
        that.refresh();
        break;
    }
  }

  onReady(options) { }

  onPullDownRefresh() {
    this.isPullDownRefreshing = true;
  }

  onReachBottom(cardCount) {
    if (cardCount > 0 && !this.isPullDownRefreshing && !this.lastPage) {
      this.getListData(this.data.nextId);
    }
  }

  refresh() {
    console.log("eventbus 名片夹刷新");
    this.getListData("");
  }

  getCardCount() {
    var that = this;
    this.cardcaseservice
      .getBizcardCount()
      .then(requestCount => {
        that
          .cardcasePage
          .setRequestCount(requestCount);
      });
  }

  getListData(nextId) {
    var that = this;
    this
      .cardcasePage
      .startPullToRefreshAnim();
    this.cardcaseservice
      .getListData(nextId)
      .then(res => {
        that
          .cardcasePage
          .stopPullToRefreshAnim(nextId == "");
        that
          .cardcasePage
          .setDataToList(nextId == "", res);
        that.nextId = res.data.nextId,
          that.lastPage = res.data.lastPage
      })
      .catch(err => {
        that
          .cardcasePage
          .stopPullToRefreshAnim(nextId);
        that.isPullDownRefreshing = false;
      });
  }

  clickStar(item) {
    if (item.collected) {
      // 判断是否已经收藏
      // 弹窗点击确定取消收藏
      this
        .cardcasePage
        .showDialog(item);
    }
  }

  cancelStar(item) {
    var that = this;
    this.cardcaseservice
      .cancelStar(item)
      .then(res => {
        // 遍历删除指定元素
        that.cardcasePage.deleteItem(item);
        that.cardcasePage.updataList(list);
        that.cardcasePage.showLoadingToast("已取消收藏");
      });
  }

  goToUri(uri) {
    wx.navigateTo({ url: uri })
  }
}