// pages/message/message.js
var nr = '';
Page({
 
  /**
   * 页面的初始数据
   */
  data: {
 
    msgData:
    [
      {
        msg:
        "送货时间太长。"
      },//双引号
      {
        msg:
        "食材不够新鲜。"
      },
      {
        msg:
        "味道不够鲜美。"
      },
      {
        msg:
        "菜做的十分精细。"
      },
      {
        msg:
        "味道鲜美，点赞！"
      },
      {
        msg:
        "看上去不错！"
      }
    ],
    neirong: '',
    msg1:'',
    username:''
 
  },
 
  clickMe: function (e) {
    var that = this;
    console.log(e);
    nr = e.currentTarget.dataset.nr;
    that.setData({
      neirong: nr
    })
  },
fnmsg:function(e){
  this.setData({
    msg1:e.detail.value
  });
},
fnneirong:function(e){
  this.setData({
    neirong:e.detail.value
  });
},
  // 留言函数开始
  liuyan:function(){
    var msg1 = this.data.msg1;
    console.log(msg1)
    var neirong = this.data.neirong;
    console.log(neirong)
    var currentusertruename=wx.getStorageSync('currentusertruename')
    console.log(currentusertruename)
    wx.request({
      url: 'http://localhost:8000/dcapi/saveliuyan',
      method: 'POST',
      data: {
        username:currentusertruename,
        msg1:msg1,
        neirong:neirong
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
       
      },
      fail(err){
        console.log(err)
      }
    });
  },
 
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
 
  },
 
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
 
  },
 
  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
 
  },
 
  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
 
  },
 
  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
 
  },
 
  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
 
  },
 
  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
 
  },
 
  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
 
  }
})