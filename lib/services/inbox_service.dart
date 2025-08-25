import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/inbox_item.dart';

class InboxService {
  final String apiUrl = 'https://api.example.com/inbox';

  Future<List<InboxItem>> fetchInboxItems() async {
    final response = await http.get(Uri.parse(apiUrl));

    if (response.statusCode == 200) {
      List<dynamic> data = jsonDecode(response.body);
      return data.map((item) => InboxItem.fromJson(item)).toList();
    } else {
      throw Exception('Failed to load inbox items');
    }
  }
}