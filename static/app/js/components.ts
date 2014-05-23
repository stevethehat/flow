/// <reference path="libdef/jquery.d.ts" />

module Flow.Components {
	'use strict';
	
    export interface IListItem {
        uid: string;
        description: string;
        icon?: string;
    }

    export interface IListItems {
        [index: number]: IListItem;
    }

    export interface IListData {
    	parentUid: string;
    	iconPath?: string;
    	items: IListItems;
    }

    export interface IViewEvent {
    	(uid: string, element: JQuery): void;
    }

    export interface IViewEventDefinition {
    	eventName: string;
    	event: IViewEvent;
    }

    export interface IViewEvents {
    	[index: number]: IViewEventDefinition;
    }

    export class BaseComponent {
		workspace: Flow.Workspace;
		container: JQuery;
		templateId: string;

		constructor(workspace: Flow.Workspace, container: JQuery) {
			this.workspace = workspace;
			this.container = container;
		}

		setEvents(events?: IViewEvents): void {
			alert('base setEvents');
		}

		render(data: any, events?: IViewEvents): void {
			this.container.empty();
			data.iconPath = this.workspace.iconPath;

			this.workspace.templates.render(this.templateId, data,
				(html: string): void => {
					this.container.html(html);
					this.setEvents(events);
				}
			);
		}
    }

	export class List extends BaseComponent {
		templateId = 'list';

		populate(list: IListData, events?: IViewEvents): void {
			this.render(list, events);
		}

		setEvents(events?: IViewEvents): void {
			this.container.find('li').click(
				(event: JQueryEventObject): void => {
					event.stopPropagation();

					var li: JQuery = $(event.target);
					this.container.find('li').removeClass('selected');

					li.addClass('selected');
				}
			);

			this.container.find('li span.list-nav').click(
				(event: JQueryEventObject): void => {
					event.stopPropagation();

					var li: JQuery = $(event.target).parent();
					this.container.find('li').removeClass('selected');

					li.addClass('selected');
				}
			);
		}
	}

	export class Popup extends BaseComponent {
		templateId = 'popup';
	}

	export class Alert extends BaseComponent {
		templateId = 'alert';
	}
}
