var Zeta=require('Zeta'),
    demo=Zeta.module('',[]);

demo.config('root',__dirname);
demo.config('public',__dirname+'/../public');
demo.l();
demo.provider('$db',{});
demo.any('static');
demo.get('/',function($scope,$render){
    $scope.res.end($render('index.html'));
});
demo.get('/str',function($scope){
    $scope.res.writeHead(200,{
        'Content-Type':'text/plain'
    });
    $scope.res.write('hello,world');
    $scope.res.end();
});
demo.get('/json',function($scope){
    $scope.res.writeHead(200,{
        'Content-Type':'application/json'
    });
    $scope.res.write({msg:"hello,world"});
    $scope.res.end();
});
demo.get('/read',function($scope,$db){

});
demo.post('write',function($scope,$db){

});
demo.app();
