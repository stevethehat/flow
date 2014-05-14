/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />
/// <reference path="server.ts" />

module Workspace{
    export class Workspace {
        constructor() {
            this.body = $('body');
            this.header = $('#header');
            this.contentArea = $('#listing1');
            if (typeof window.innerWidth != 'undefined') {
                this.width = window.innerWidth,
                this.height = window.innerHeight
            }            
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
                        { description: 'hello1', uid: '2'},
                        { description: 'hello2', uid: '3'},
                    ]
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
    }

    $(document).ready(
        function(){
            var workspace: Workspace = new Workspace();        
        }
    );
}