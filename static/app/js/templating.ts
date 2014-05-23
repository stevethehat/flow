/// <reference path="jquery.d.ts" />
/// <reference path="handlebars.d.ts" />

module Templates{
	interface TemplatesList{
		[index: string]: HandlebarsTemplateDelegate;
	}

	export class Templates{
		private workspace: Workspace.Workspace;
		private templateCache: JQuery;
		private templates: TemplatesList;

		constructor(workspace: Workspace.Workspace){
			this.workspace = workspace;
			this.templates = {};

			Handlebars.registerHelper('iconPath', 
				(icon) => {
					return(this.workspace.iconPath + '/32x32/' + icon + '.png');
				}	
			);
		}

		render(id: string, data: any, result: any){
			var html: string = '';
			var template: HandlebarsTemplateDelegate;

			if(this.templates[id]){
				template = this.templates[id];
				result(template(data));
			} else {
				$.get('/html/templates/' + id + '.htm',
					(templateCode: string) => {
						template = Handlebars.compile(templateCode);
						this.templates[id] = template;
						result(template(data));
					}
				);
			}
		}
	}
}