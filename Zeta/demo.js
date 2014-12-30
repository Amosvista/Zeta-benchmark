var Zeta=require('zeta'),
    demo=Zeta.module('',[]);

var data=require('./db.js'),
    User=data.User,
    Book=data.Book;
User.findOne({name:'suemi'},function(err,doc){
    if(!err&&!doc){
        var user= new User({name:'suemi',passwd:'******'});
        user.save();
    }
});
demo.config('root',__dirname);
demo.config('public',__dirname+'/../public');
demo.l();
demo.provider('$db',{});
demo.any('static');
demo.guard.get().post().with(function(){
    console.log('error occurs');
});
demo.get('/',function($scope,$render){
    $scope.res.end($render('index.html'));
});
demo.get('/str',function($scope){
    $scope.send('hello,world').end();
});
demo.get('/json',function($scope){
    $scope.send({msg:"Hello,World!"});
});
demo.get('/read',function($scope){
    User.findOne({name:'suemi'},function(err,doc){
        if(err) $scope.send('fail');
        else $scope.send(doc);
    });
});
demo.post('write',function($scope){
    var tmp=Math.floor(Math.random()*10000);
    Book.findOne({serial:tmp},function(err,doc){
        if(!doc){
            (new Book({serial:tmp,money:400})).save(function(err,doc){
                if(!err) $scope.send('success');
                else $scope.send('fail');
            });
        }
        else{
            doc.money=400;
            doc.save(function(err,doc){
                if(!err) $scope.send('success');
                else $scope.send('fail');
            });
        }
    });
});
demo.h('h0',function($scope){
    $scope.str="";
    $scope.go('next');
});
demo.h('h1',function($scope){
    $scope.str+="0";
    $scope.go('next');
});
demo.h('h2',function($scope){
    $scope.str+="1";
    $scope.go('next');
});
demo.h('h3',function($scope){
    $scope.str+="2";
    $scope.go('next');
});
demo.h('h4',function($scope){
    $scope.send($scope.str);
});
demo.get('/chain',['h0','h1','h2','h3','h4']);
demo.app();
