import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'All Ears',
      theme: ThemeData(
        primaryColor: const Color.fromARGB(255, 203, 66, 24),
        colorScheme: ColorScheme.fromSwatch(
          primarySwatch: Colors.deepOrange,
          ).copyWith(
            secondary: const Color.fromARGB(255, 203, 66, 24),
            ),),

      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("All Ears")),
      body: const Center(
        child: Text("👋 My Q&A app"),
      ),
    );
  }
}
