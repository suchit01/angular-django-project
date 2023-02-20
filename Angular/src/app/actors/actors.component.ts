import { Component } from '@angular/core';
import { ApiServiceService } from '../api-service.service';

@Component({
  selector: 'app-actors',
  templateUrl: './actors.component.html',
  styleUrls: ['./actors.component.css']
})
export class ActorsComponent {
  title = 'Actors List';
  data: any;
  displayedColumns: string[] = ["No", 'name', 'dob', 'num_movies'];

  constructor(private _apiService: ApiServiceService){}

  ngOnInit(){
    this._apiService.getActorsData().subscribe(res=>{
      this.data=res;
    })
  }
}
