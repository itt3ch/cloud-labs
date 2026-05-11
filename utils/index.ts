const API_URL =
  "https://mysupercontainerapp.agreeablepebble-48827771.spaincentral.azurecontainerapps.io";

const AUTH_TOKEN = "";

interface Pizza {
  id: number;
  name: string;
  description: string;
  price: number;
  size: string;
  ingredients: string[];
}

const payload: Pizza = {
  id: 0,
  name: "string",
  description: "string",
  price: 0,
  size: "string",
  ingredients: ["string"],
};

const TOTAL_REQUESTS = 1000;

async function sendRequest(index: number): Promise<void> {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${AUTH_TOKEN}`,
    },
    body: JSON.stringify(payload),
  });

  console.log(`Request ${index + 1}: ${response.status}`);
}

(async () => {
  const tasks: Promise<void>[] = [];

  for (let i = 0; i < TOTAL_REQUESTS; i++) {
    tasks.push(sendRequest(i));
  }

  await Promise.all(tasks);
})();