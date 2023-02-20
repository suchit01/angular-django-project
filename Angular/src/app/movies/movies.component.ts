import { Component } from '@angular/core';
import { ApiServiceService } from '../api-service.service';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.css']
})
export class MoviesComponent {
  title = 'Movies List';
  data: any;
  displayedColumns: string[] = ['No', 'title', 'desc', 'release_date', 'num_actors', 'upvotes', 'downvotes'];
  selected = "title"; 
  
  constructor(private _apiService: ApiServiceService){}

  sortData(field: any) {
    this.data = this.data.sort((a: any,b: any)=> (a[field] < b[field]) ? -1 : 1)
  }

  upVote(id: any){
    this._apiService.upVote(id).subscribe(res=>{
      // console.log(res);
      this.ngOnInit(this.selected);
    })
  }

  downVote(id: any){
    this._apiService.downVote(id).subscribe(res=>{
      // console.log(res);
      this.ngOnInit(this.selected);
    })
  }

  ngOnInit(field: any = "title"){
    this.selected = field;
    this._apiService.getMoviesData().subscribe(
      res=>{
        this.data=res;
        this.sortData(this.selected);
      }
    );
  }
}
