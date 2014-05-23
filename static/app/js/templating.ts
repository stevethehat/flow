/// <reference path="jquery.d.ts" />
/// <reference path="handlebars.d.ts" />

module Templates{
	interface TemplatesList{
		[index: number]: HandlebarsTemplateDelegate;
	}
	
	export class Templates{
		_workspace: Workspace.Workspace;
		_templateCache: JQuery;
		private _templates: TemplatesList;

		constructor(workspace: Workspace.Workspace){
			this._workspace = workspace;
			this._templates = {};

			Handlebars.registerHelper('iconPath', 
				(icon) => {
					return(this._workspace.iconPath + '/32x32/' + icon + '.png');
				}	
			);
		}

		render(id: string, data: any, result: any){
			var html: string = '';
			var template: HandlebarsTemplateDelegate;

			if(this._templates[id]){
				template = this._templates[id];
				result(template(data));
			} else {
				//var template: any;
				$.get('/html/templates/' + id + '.htm',
					(templateCode: string) => {
						template = Handlebars.compile(templateCode);
						this._templates[id] = template;
						result(template(data));
					}
				);
			}
		}
	}
}