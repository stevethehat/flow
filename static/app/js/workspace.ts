/// <reference path="libdef/jquery.d.ts" />
/// <reference path="menus.ts" />
/// <reference path="server.ts" />

module Flow {
    'use strict';

    export class Workspace {
        private body: JQuery;
        private header: JQuery;
        private contentArea: JQuery;
        private footer: JQuery;
        private server: Server.Server;
        private listview: Flow.Components.List;
        private alert: Flow.Components.Alert;
        private width: number;
        private height: number;
        
        public iconPath: string = '/assets/icons';
        public templates: Flow.Templates.Templates;

        constructor() {
            this.body = $('body');
            if (typeof window.innerWidth !== 'undefined') {
                this.width = window.innerWidth;
                this.height = window.innerHeight;
            }

            this.templates = new Flow.Templates.Templates(this);
            this.server = new Server.Server('localhost', 'html');

            this.templates.render('main', {},
                (mainContent: string): void => {
                    this.body.html(mainContent);
                    this.header = $('#header');
                    this.header = $('#footer');
                    this.contentArea = $('.main-content');

                    this.contentArea.height(this.height - this.header.height() - 60);
                    this.listview = new Flow.Components.List(this, this.contentArea);

                    this.server.get('1', 'workspacemenu', null,
                        (data: any): void => {
                            // mainMenu.populate(<Actions.ActionElements>data);
                        }
                    );
                    this.navigate('1');
                }
            );
        }

        log(): void{
            alert('in log');
        }

        navigate(uid: string): void {
            this.listview.populate(
                {
                    parentUid: '1',
                    items: [
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
                            event: function(uid: string, item: JQuery): void {
                                // this.listview.setSelected(item);
                            }
                        },
                        {
                            eventName: 'navigate',
                            event: function(): void {
                                alert('nav clicked');
                            }
                        }
                    ]
                }
            );
        }

        runAction(): void {
            alert('run action');
        }
    }

    $(document).ready(
        function(): void {
            var workspace: Workspace = new Workspace();
        }
    );
}
