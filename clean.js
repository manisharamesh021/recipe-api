const fs = require("fs");

// Read data.json file
const rawData = fs.readFileSync("data.json");
const data = JSON.parse(rawData);

// Convert object to array
const cleanedData = Object.keys(data).map((key) => {
  const item = data[key];

  // function to get number from "389 kcal"
  function getNumber(value) {
    if (!value) return null;
    const match = value.match(/\d+/);
    return match ? Number(match[0]) : null;
  }

  return {
    id: Number(key),
    continent: item.Contient,
    country: item.Country_State,
    cuisine: item.cuisine,
    title: item.title,
    url: item.URL,
    rating: Number(item.rating),
    total_time: Number(item.total_time),
    prep_time: Number(item.prep_time),
    cook_time: item.cook_time ? Number(item.cook_time) : null,
    description: item.description,
    ingredients: item.ingredients,
    instructions: item.instructions,

    calories: getNumber(item.nutrients?.calories),
    carbohydrate: getNumber(item.nutrients?.carbohydrateContent),
    cholesterol: getNumber(item.nutrients?.cholesterolContent),
    fiber: getNumber(item.nutrients?.fiberContent),
    protein: getNumber(item.nutrients?.proteinContent),
    saturated_fat: getNumber(item.nutrients?.saturatedFatContent),
    sodium: getNumber(item.nutrients?.sodiumContent),
    sugar: getNumber(item.nutrients?.sugarContent),
    fat: getNumber(item.nutrients?.fatContent),

    servings: getNumber(item.serves)
  };
});

// Save cleaned file
fs.writeFileSync(
  "cleanedData.json",
  JSON.stringify(cleanedData, null, 2)
);

console.log("Cleaning completed!");
