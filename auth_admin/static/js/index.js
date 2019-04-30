new Vue({
    el: '#index',
    data: {
        topmenu: [], //[{ "id": 9, "title": "fuchuanqi", "url": --- }, { "id": 10, "get_data": "hello" }]
        banner: [],
        get_data:[], // [{ "id": 9, "get_data": "fuchuanqi" }, { "id": 10, "get_data": "hello" }]
        now_data:{},  // { "id": 10, "get_data": "hello" }
        userUI: true,
        // {title:'首页'}, {title:'博客'}, {title:'作品'}, {title:'联系'}
    },

    methods:{
        //ajax得到动态数据
        getData:function () {
            // var self = this;
            reqwest({
                url:'/api/index',
                method: 'get',
                type: 'json',
                success: (data)=>{
                    // console.log(data);
                    this.topmenu = data.topmenu;
                    // this.topmenu_url = data.topmenu.url;
                    // console.log(this.topmenu);
                    // console.log(self.topmenu)
                    this.banner = data.banner;
                    this.get_data = data.get_data;
                    this.now_data = data.get_data[this.get_data.length-1]   //列表最后一个字典元素
                    // if (this.get_data[this.get_data.length-1].id > this.now_data_id)
                    //     this.now_data_id = this.get_data[-1].id;
                    // console.log(data)
                    // console.log(this.get_data[(this.get_data.length)-1])  //列表最后一个字典元素
                }
            })
        },

        // nowdata:function () {
        //     this.now_data_id = this.get_data[0].id
        // }
        showUserUI:function () {
            this.userUI = !this.userUI;
        },
    },

     mounted(){
        // console.log(this.topmenu);

                // var _this = this;
                this.timer = setInterval(()=>{
                    this.getData();
                },1000)

        // console.log(this)
    },
    beforeDestroy: function () {
                if (this.timer){
                    clearInterval(this.timer);
                }
            }
});

// new Vue({
//   delimiters:['[[',']]'],
//   el:'#index',
//   data:{
//     topmenu:[],
//     banner:[],
//     userUI:false,
//     loginType:false,
//     username:'',
//     password:''
//   },
//   mounted(){
//     this.getData()
//     console.log(this)
//   },
//   methods:{
//     getData:function(){
//       var self = this
//       reqwest({
//         url:'/api/index',
//         method: 'get',
//         type:'json',
//         success:function(data){
//           console.log(data)
//           self.topmenu = data.topmenu
//           self.banner = data.banner
//           if(data.loginType == 'ok'){
//             self.loginType = true
//           }else{
//             self.loginType = false
//           }
//           // console.log(self.topmenu)
//         }
//       })
//     },
//     userLogin:function(){
//       var self = this
//       reqwest({
//         url:'/api/index',
//         method:'post',
//         type:'json',
//         headers:{
//           "X-CSRFTOKEN":csrftoken
//         },
//         data:{
//           username:self.username,
//           password:self.password
//         },
//         success:function(data){
//           console.log('ok');
//           console.log(data);
//           if (data.loginType=='ok') {
//             self.userUI = false;
//             self.loginType = true
//           }
//         },
//         error:function(err){
//           console.log(err)
//         }
//       })
//     },
//     showUserUI:function(){
//       this.userUI = !this.userUI
//     },
//     toadmin:function() {
//       window.location.href = '/Dwebadmin'
//     }
//   }
// });
