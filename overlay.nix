final: prev: with final;
{

  mypython = with prev.python310Packages; [
    flake8
    black

    pandas
    requests
    beautifulsoup4
  ];

}
