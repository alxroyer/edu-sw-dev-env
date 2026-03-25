// src/main.rs

use axum::{routing::get, Router, extract::Query};
use serde::Deserialize;

// Define '/hello' parameters.
#[derive(Deserialize)]
struct HelloParams {
    // Consider an optional `name` parameter.
    name: Option<String>,
}

/**
 * '/hello' endpoint handler.
 */
async fn hello(Query(params): Query<HelloParams>) -> String {
    // Trace the query.
    println!("/hello requested");

    // Return the result.
    match params.name {
        Some(name) => format!("Hello {}!", name),
        None => "Hello stranger!".to_string(),
    }
}

#[tokio::main]
async fn main() {
    // Create an axum router.
    let app = Router::new()
        // Handle the '/hello' endpoint.
        .route("/hello", get(hello));

    // Launch the server on localhost:3000.
    let listener = tokio::net::TcpListener::bind("localhost:3000").await.unwrap();
    println!("Server started on http://localhost:3000");
    axum::serve(listener, app).await.unwrap();
}
