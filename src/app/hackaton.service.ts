import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {catchError, map, tap} from 'rxjs/operators';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import {User} from './user'

const httpOptions = {headers: new HttpHeaders({'Content-Type': 'application/json'})};



@Injectable({
  providedIn: 'root'
})
export class HackatonService {
  private hackatonURL = 'localhost/'

  constructor(
    private http: HttpClient,
  ) { }
  
  getItems(): Observable<User[]>{
    return this.http.get<User[]>(this.hackatonURL);
  }

  getItem(id: number): Observable<User>{
    const url= `${this.hackatonURL}${id}`;
    return this.http.get<User>(url);
  }

  postItem(item: User): Observable<User>{
    return this.http.post<User>(this.hackatonURL, item, httpOptions);
  }

  updateItem(item: User): Observable<any>{
    const id = typeof item === 'number' ? item : item.id;
    const url = `${this.hackatonURL}${id}`;
    return this.http.put(url, item, httpOptions);
  }

  deleteItem(item: User | number): Observable<User> {
    const id = typeof item === 'number' ? item : item.id;
    const url = `${this.hackatonURL}${id}`;

    return this.http.delete<User>(url, httpOptions);
  }


}
