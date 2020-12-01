//app.js
App({
  onLaunch: function () {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo
              console.log(res.userInfo)

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },
  onShow:function(){
    //在此处写的代码，当小程序成为当前运行的界面，就会调用此处的代码
  },
  onHide:function(){
    //当你打开小程序，然后切换到其他应用程序的时候，就会调用此处的代码
  },
  onError:function(){
      // wx.redirectTo({
      //   url: '/pages/test/test'
      // });//当页面脚本出错的时候，小程序跳转到指定的页面。不允许跳转到 tabbar 页面
      //从A页面跳转到B页面的时候，把A页面关闭，把B页面打开。

      wx.switchTab({
        url: '/pages/index/index',
      })
    },
  globalData: {
    userInfo: null,
    username:"tangyan",
    sex:"boy"
  }
})