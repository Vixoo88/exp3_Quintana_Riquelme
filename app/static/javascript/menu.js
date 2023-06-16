fetch('https://www.themealdb.com/api/json/v1/1/filter.php?c=Breakfast')
      .then(response => response.json())
      .then(data => {
        const menu = document.getElementById('menu');
        data.meals.forEach(meal => {
          const li = document.createElement('li');
          const img = document.createElement('img');
          img.src = meal.strMealThumb;
          li.appendChild(img);
          const span = document.createElement('span');
          span.textContent = meal.strMeal;
          li.appendChild(span);
          menu.appendChild(li);
        });
      });