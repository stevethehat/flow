/// <reference path="jquery.d.ts" />

module Listings{
    export interface ListItem {
        uid: string;
        description: string;
        icon?: string;
    }

    export interface ListItems {
        [index: number]: ListItem;
    }

    export interface List{
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
		_workspace: Workspace.Workspace;
		_container: JQuery;
		constructor(workspace: Workspace.Workspace, container: JQuery){
			this._workspace = workspace;
			this._container = container;
		}

		setEvents(events?: ViewEvents): void{
			alert('base setEvents');
		}

		populate(list: List, events?: ViewEvents){
			this._container.empty();
			list.iconPath = this._workspace.iconPath;

			this._workspace.template.render('list', list,
				(html) => {
					this._container.html(html);
					this.setEvents(events);
				}
			);
		}		
    }

	export class ListView extends View{
		setEvents(events?: ViewEvents): void{
			this._container.find('li').click((event: JQueryEventObject) => {
					event.stopPropagation();

					var li: JQuery = $(event.target);
					var uid: string = li.attr('data-flowuid');

					this._container.find('li').removeClass('selected');

					li.addClass('selected');
				}
			);

			this._container.find('li span.list-nav').click((event: JQueryEventObject) => {
					event.stopPropagation();

					var li: JQuery = $(event.target).parent();
					var uid: string = li.attr('data-flowuid');

					this._container.find('li').removeClass('selected');

					li.addClass('selected');
				}
			);					
		}
	}
}