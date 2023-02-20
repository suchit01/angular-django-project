import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class ApiServiceService {

  constructor(private _http: HttpClient) { }

  upVote(id: any) {
    let url = 'http://localhost:8000/api/movies/' + id;
    return this._http.put(url, {"is_upvote": true});
  }

  downVote(id: any) {
    let url = 'http://localhost:8000/api/movies/' + id;
    return this._http.put(url, {"is_downvote": true});
  }

  getMoviesData() {
    return this._http.get('http://localhost:8000/api/movies');
  }

  getActorsData() {
    return this._http.get('http://localhost:8000/api/actors');
  }
}
