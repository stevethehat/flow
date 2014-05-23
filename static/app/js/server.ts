/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />

module Flow.Server{
	export class Server{
		constructor(host: string, baseUrl: string){
			this._host = host;
			this._baseUrl = baseUrl;
		}

		private _host: string;
		private _baseUrl: string;

		get(uid: string, action: string, data: any, callback: any): void{
			var url: string = '/' + this._baseUrl + '/' + uid + '/' + action;
			var ajaxParameters = {
				url: url,
				success: function (data) {
					callback(data);
				},
				error: function (XMLHttpRequest, textStatus, errorThrown) {
					alert('Error (' + url + ') ' + XMLHttpRequest.responseText + ' ' + textStatus + ' ' + errorThrown);
				}
			}
			$.ajax(ajaxParameters);
		}	
	}
}
