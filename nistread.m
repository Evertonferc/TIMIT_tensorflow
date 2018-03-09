% function [signal, fs, bits, begins, version] = nistread(filename)
% Read a NIST file (it does not treat multi-channel files yet).
% It is based on TIMIT files avaliable in CD-ROM, which are 16 bits,
% monoaural audio files.
% 
% Inputs:
% -------
% filename:    name of the files
% 
% Outputs:
% --------
% signal   vector/matrix containing the signal read from filename
% fs       its sampling rate
% bits     its bits/sample (always 32)
% begins   the delay of first samples of signal
% version  version of nist file
function [signal, fs, bits, begins, version] = nistread(filename)

fid = fopen(filename, 'r'); %abr arquivos com leitura binária e retorna um inteiro igual ou maior q 3 pq o matlab
%reserva 0, 1 e 2 para entrada padrao, saida padrao (tela) e erro padrao,
%respectivamente
if fid==-1
    error('arquivo [%s] não pode ser aberto', filename);
end

% reading and treating header data
header = char(fread(fid, 16, 'char')');%le dados de um vetor A e a posição do apontador de arquivo é o marcador do final do arquivo
%o arquivo binário é indicado pelo fid (fopen). 16 é o tamanho do array
if strcmpi(header(1:5), 'NIST_')==0 %compara duas strings, no caso ele tenta ver se o header é NIST_ e compara com 0, ou seja, se n forrem iguais, retorna erro
    fclose(fid);
    error('arquivo [%s] não está no formato NIST', filename);
end

version = header(6:7);
header_size = str2double(header(9:15));

header = char(fread(fid, header_size - 16, 'char')');
header_data = regexp(header, 'sample_rate -i (?<fs>\w+)', 'names');
if isempty(header_data)
    fs = 1;
else
    fs = str2double(header_data.fs);
end

header_data = regexp(header, 'sample_sig_bits -i (?<bits>\w+)', 'names');
if isempty(header_data)
    fclose(fid);
    error('Unknown bits per sample');
else
    bits = str2double(header_data.bits);
end

% reading data in little-endian format
if bits==16
    signal = fread(fid, Inf, 'int16', 'l');
elseif bits==8
    signal = fread(fid, Inf, 'int8', 'l');
else
    fclose(fid);
    error('Unable to read data in the provided bits/sample');
end

fclose(fid);

begins = 0;