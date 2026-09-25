const { test, expect } = require("@playwright/test");

test("core planner flow works in English and Russian", async ({ page }) => {
  await page.goto("/");
  await expect(page).toHaveTitle(/MINI — Focus Planner/);

  await page.locator("#focus").fill("Launch the product");
  await page.locator("#p1").fill("Finish the listing");
  await page.locator("#addTask").click();
  await page.locator("#tasks input[type=text]").first().fill("Check the files");
  await page.locator("#tasks .check").first().check();
  await expect(page.locator("#score")).toHaveText("100%");

  await page.locator("#lang").selectOption("ru");
  await expect(page.locator("#addTask")).toHaveText("+ Добавить задачу");
  await expect(page.locator("#focusTitle")).toHaveText("Launch the product");
  await expect(page.locator("#notes")).toHaveAttribute("placeholder", "Идеи, напоминания, важные мысли...");

  await page.reload();
  await expect(page.locator("#focus")).toHaveValue("Launch the product");
  await expect(page.locator("#p1")).toHaveValue("Finish the listing");
  await expect(page.locator("#tasks input[type=text]").first()).toHaveValue("Check the files");
});
