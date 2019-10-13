A little game using <a href="https://github.com/kitao/pyxel">Pyxel by kitao</a>
It use <b>Raycast</b> for collison detection, each cells in the tilemap will get 4 walls assigned to it and the rays will pass the walls as a way to detect collision, by returning a point of intersection and a distance from that point.

By getting the data from the tilemap we can assign different wall from a given cells like slope or different ways to interact with the cells, clibing area, water or different type of cells.
