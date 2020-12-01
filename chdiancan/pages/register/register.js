// pages/register/register.js

Page({
 
  /**
   * 页面的初始数据
   */
  data: {
    username:'',
    truename:'',
    tel:'',
    address:'',
    NewChanges: '',
    NewChangesAgain: '',
    success: false
  },

  return_home: function (e) {
    wx.navigateTo({
      url: '/pages/login/login',
    })
 
  },
  handleInputusername: function (e) {
    this.setData({
      username: e.detail.value
    })
  },
  handleInputtruename: function (e) {
    this.setData({
      truename: e.detail.value
    })
  },
  handleInputtel: function (e) {
    this.setData({
      tel: e.detail.value
    })
  },
  handleInputaddress: function (e) {
    this.setData({
      address: e.detail.value
    })
  },
  handleNewChanges: function (e) {
    console.log(e);
    this.setData({
      NewChanges: e.detail.value
    })
  },
  handleNewChangesAgain: function (e) {
    console.log(e);
    this.setData({
      NewChangesAgain: e.detail.value
    })
 
  },


 
  submit: function (e) {
    var that = this
      if (this.data.NewChanges == '') {
      wx.showToast({
        title: '请输入您的信息',
        image: '/pages/img/error.png',
        duration: 2000
      })
      return
    } else if (this.data.NewChangesAgain != this.data.NewChanges) {
      wx.showToast({
        title: '两次密码不一致',
        image: '/images/error.png',
        duration: 2000
      })
      return
    } else {
      var that = this
      var phone = that.data.phone;
      wx.request({
        url: 'http://localhost:8000/dcapi/register',
        method: 'POST',
        data: {
          username: that.data.username,
          truename: that.data.truename,
          tel: that.data.tel,
          address: that.data.address,
          password: that.data.NewChanges,
          // NewChangesAgain: that.data.NewChangesAgain,
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        success: function (res) {
          wx.showToast({
            title: '提交成功~',
            icon: 'loading',
            duration: 2000
          })
          // console.log(username)
          console.log(res)
          that.setData({
            success: true
          })
        }
      })
    }
  },
  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
 
  }
})