/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />
/// <reference path="server.ts" />

module Workspace{
    export class Workspace {
        constructor() {
            this.body = $('body');
            var self: Workspace = this;

            if (typeof window.innerWidth != 'undefined') {
                this.width = window.innerWidth,
                this.height = window.innerHeight
            }       

            this.template = new Templates.Template(this);  
            self.initialize();
        }
        initialize(){
            this.header = $('#header');
            this.contentArea = $('#listing1');

            this.contentArea.height(this.height - this.header.height() -60);
            this.listview = new Listings.ListView(this, this.contentArea);

            this.server = new Server.Server("localhost", "html");
            this.server.get("1", "workspacemenu", null, 
                function(data){
                    //mainMenu.populate(<Actions.ActionElements>data);
                }
            );
            this.navigate('1');            
        }
        log(): void{
            alert('in log');
        }
        navigate(uid: string){
            this.listview.populate(
                {
                    parentUid: '1',
                    items:[
                        { description: 'hello1', uid: '2', icon: 'beer'},
                        { description: 'hello2', uid: '3', icon: 'bell'},
                    ]
                },
                function(uid: string, item: JQuery){
                    //alert('select');
                    //this.listview.setSelected(item);
                    //alert('after call');
                },
                function(){ 
                    //alert('navigate');
                }
            );
        }
        runAction(){


        }
        body: JQuery;
        header: JQuery;
        contentArea: JQuery;
        footer: JQuery;
        server: Server.Server;
        listview: Listings.ListView;
        width: number;
        height: number;
        iconPath: string = '/assets/icons';
        template: Templates.Template;
    }

    $(document).ready(
        function(){
            var workspace: Workspace = new Workspace();        
        }
    );
}