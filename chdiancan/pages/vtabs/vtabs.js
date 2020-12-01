Page({
  data: {
    vtabs: [],
    vtabcontents:[],
    activeTab: 0,
  },
  fngotoshopcar: function(e){
   
    
  },
  fnbinddata:function(){
    var that=this;
    wx.request({
      url: 'http://localhost:8000/dcapi/getdrinklist',
      method: 'POST',
      data: { },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data);
        that.setData({
          vtabcontents:cc.data
        });
      }
    });
  },
  onLoad() {
    const titles = ['饮料', '啤酒', '白酒',
      '红酒']
    const vtabs = titles.map(item => ({title: item}))
    this.setData({
      vtabs:vtabs
    });
    this.fnbinddata(); 
  },

  onTabCLick(e) {
    const index = e.detail.index
    console.log('tabClick', index)
  },

  onChange(e) {
    const index = e.detail.index
    console.log('change', index)
  }

})
