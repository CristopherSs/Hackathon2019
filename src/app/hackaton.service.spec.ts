import { TestBed } from '@angular/core/testing';

import { HackatonService } from './hackaton.service';

describe('HackatonService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: HackatonService = TestBed.get(HackatonService);
    expect(service).toBeTruthy();
  });
});
