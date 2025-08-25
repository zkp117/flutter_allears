class InboxItem {
  final String title;
  final String message;
  final String date;

  InboxItem({
    required this.title,
    required this.message,
    required this.date,
  });

  factory InboxItem.fromJson(Map<String, dynamic> json) {
    return InboxItem(
      title: json['title'] ?? 'No Title',
      message: json['message'] ?? '',
      date: json['date'] ?? '',
    );
  }
}
