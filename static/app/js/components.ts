/// <reference path="jquery.d.ts" />

module Components{
    export interface ListItem {
        uid: string;
        description: string;
        icon?: string;
    }

    export interface ListItems {
        [index: number]: ListItem;
    }

    export interface ListData{
    	parentUid: string;
    	iconPath?: string;
    	items: ListItems;
    }

    export interface ViewEvent{
    	(uid: string, element: JQuery): void;
    }

    export interface ViewEventDefinition{
    	eventName: string;
    	event: ViewEvent;
    }

    export interface ViewEvents{
    	[index: number]: ViewEventDefinition;
    }

    export class View{
		workspace: Workspace.Workspace;
		container: JQuery;

		constructor(workspace: Workspace.Workspace, container: JQuery){
			this.workspace = workspace;
			this.container = container;
		}

		setEvents(events?: ViewEvents): void{
			alert('base setEvents');
		}

		populate(list: ListData, events?: ViewEvents){
			this.container.empty();
			list.iconPath = this.workspace.iconPath;

			this.workspace.templates.render('list', list,
				(html) => {
					this.container.html(html);
					this.setEvents(events);
				}
			);
		}		
    }

	export class List extends View{
		setEvents(events?: ViewEvents): void{
			this.container.find('li').click((event: JQueryEventObject) => {
					event.stopPropagation();

					var li: JQuery = $(event.target);
					var uid: string = li.attr('data-flowuid');

					this.container.find('li').removeClass('selected');

					li.addClass('selected');
				}
			);

			this.container.find('li span.list-nav').click((event: JQueryEventObject) => {
					event.stopPropagation();

					var li: JQuery = $(event.target).parent();
					var uid: string = li.attr('data-flowuid');

					this.container.find('li').removeClass('selected');

					li.addClass('selected');
				}
			);					
		}
	}
}