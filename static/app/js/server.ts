/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />

module Server{
	export class Server{
		constructor(host: string, baseUrl: string){
			this._host = host;
			this._baseUrl = baseUrl;
		}

		private _host: string;
		private _baseUrl: string;

		get(uid: string, action: string, data: any, callback: any): void{
			var ajaxParameters = {
				url: '/' + this._baseUrl + '/' + uid + '/' + action,
				success: function (data) {
					alert(data);
				},
				error: function (XMLHttpRequest, textStatus, errorThrown) {
					//console.log('Bridge.error');
					//console.log('Response Text: ' + XMLHttpRequest.responseText);
					//Util.serverError(XMLHttpRequest.responseText);
					//console.log('Text Status: ' + textStatus);
					//console.log('Error Thrown: ' + errorThrown);
					//self.processQueue();
					alert('error');
				}
			}

			$.ajax(ajaxParameters);
		}	
	}
}
