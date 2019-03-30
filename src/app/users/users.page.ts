import { Component, OnInit } from '@angular/core';
import { Damaged } from '../damaged';
import {HackatonService} from '../hackaton.service'

@Component({
  selector: 'app-users',
  templateUrl: './users.page.html',
  styleUrls: ['./users.page.scss'],
})
export class UsersPage implements OnInit {
  public damaged: Damaged = new Damaged();
  constructor(
    private hackatonService: HackatonService,
  ) { }
  show() {
    console.log(this.damaged.user_id);  
    console.log(this.damaged.email);
    console.log(this.damaged.password);
    console.log(this.damaged.name);
    console.log(this.damaged.last_name);
    console.log(this.damaged.gender);
    console.log(this.damaged.disability);

    console.log(JSON.stringify(this.damaged)) ;
  }
  ngOnInit() {
  }
  add(): void {
    console.log(this.damaged)
    this.hackatonService.postItem(this.damaged); 
      /* .subscribe(damaged => {
        this.damaged.push(damaged as unknown as Damaged);
      }); */
  }

}
