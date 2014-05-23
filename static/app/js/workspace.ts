/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />
/// <reference path="server.ts" />

module Workspace{
    export class Workspace {
        private body: JQuery;
        private header: JQuery;
        private contentArea: JQuery;
        private footer: JQuery;
        private server: Server.Server;
        private listview: Listings.ListView;
        private width: number;
        private height: number;
        
        public iconPath: string = '/assets/icons';
        public templates: Templates.Templates;

        constructor() {
            this.body = $('body');
            if (typeof window.innerWidth != 'undefined') {
                this.width = window.innerWidth,
                this.height = window.innerHeight
            }       

            this.templates = new Templates.Templates(this);  
            this.server = new Server.Server("localhost", "html");

            this.templates.render('main',{},
                (mainContent) => {
                    this.body.html(mainContent);
                    this.header = $('#header');
                    this.contentArea = $('#listing1');

                    this.contentArea.height(this.height - this.header.height() -60);
                    this.listview = new Listings.ListView(this, this.contentArea);

                    this.server.get("1", "workspacemenu", null, 
                        function(data){
                            //mainMenu.populate(<Actions.ActionElements>data);
                        }
                    );
                    this.navigate('1'); 
                }
            )
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
                        { description: 'hello2', uid: '3', icon: 'bell', 
                            summary: 'this is the summary... this is the summary... this is the summary... this is the summary... this is the summary... this is the summary... this is the summary... this is the summary... this is the summary...'
                        },
                    ]
                },
                {
                    events: [
                        {
                            eventName: 'select',
                            event: function(uid: string, item: JQuery){
                                //this.listview.setSelected(item);
                            }   
                        },
                        {
                            eventName: 'navigate',
                            event: function(){}
                        } 
                    ]
                }
            );
        }

        runAction(){

        }
    }

    $(document).ready(
        function(){
            var workspace: Workspace = new Workspace();        
        }
    );
}