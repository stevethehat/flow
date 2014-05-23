/// <reference path="libdef/jquery.d.ts" />
/// <reference path="libdef/handlebars.d.ts" />

module Flow.Templates {
	'use strict';
	
	interface ITemplatesList {
		[index: string]: HandlebarsTemplateDelegate;
	}

	export class Templates {
		private workspace: Workspace;
		private templates: ITemplatesList;

		constructor(workspace: Workspace) {
			this.workspace = workspace;
			this.templates = {};

			Handlebars.registerHelper('iconPath',
				(icon: string): string => {
					return(this.workspace.iconPath + '/32x32/' + icon + '.png');
				}
			);
		}

		render(id: string, data: any, result: any): void {
			var template: HandlebarsTemplateDelegate;

			if(this.templates[id]) {
				template = this.templates[id];
				result(template(data));
			} else {
				$.get('/html/templates/' + id + '.htm',
					(templateCode: string): void => {
						template = Handlebars.compile(templateCode);
						this.templates[id] = template;
						result(template(data));
					}
				);
			}
		}
	}
}
